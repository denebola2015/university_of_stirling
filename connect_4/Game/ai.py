""" This module provides a function to get the AI's suggested move in the Connect 4 game. It Sends the current 'gameplay' matrix 
to both OpenAI's GPT model and DeepSeek's API and - depending on successful connection to anyone of these, returns the AI's suggested move. 
Both the 'OPENAI_API_KEY' and 'DEEPSEEK_API_KEY' environment variable are set locally on my computer. Any porting of this code to another environment
will require setting up an OpenAI API key or DeepSeek API key in the environment variables for the code to function correctly.
The gameplay_matrix is a numpy array representing the Connect 4 board.
                         0 = empty, 1 = Red (player), 2 = Yellow (AI).
Added lru caching to optimize repeated calls with the same board state. lru decorator caches up to 128 unique board states.
"""
import os
from openai import OpenAI
from functools import lru_cache
import numpy as np
# --- Module-level client initialization ---
# Initialize the client once when the module is imported for efficiency.git
# This also helps in failing early if the API key is not set.
try:
    # Check for DeepSeek specific key first, then fall back to the general OpenAI key name.
    API_KEY = os.environ.get('DEEPSEEK_API_KEY') or os.environ.get('OPENAI_API_KEY')
    if not API_KEY:
        print("Warning: DEEPSEEK_API_KEY or OPENAI_API_KEY environment variable not found. AI will not function.")
        client = None
    else:
        client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None

def get_ai_move(gameplay_matrix: np.ndarray, valid_moves: list) -> int:
    """
    Public-facing function to get the AI's move.
    It converts the NumPy array to a hashable tuple before calling the cached function.
    Args:
        gameplay_matrix: The current board state.
        valid_moves: A list of column indices that are not full.
    """
    # Convert the numpy array to a tuple of tuples to make it hashable for the cache.
    board_tuple = tuple(map(tuple, gameplay_matrix))
    # Also convert the list of valid moves to a tuple to make it hashable.
    valid_moves_tuple = tuple(valid_moves)
    return _get_ai_move_cached(board_tuple, valid_moves_tuple)

@lru_cache(maxsize=128)
def _get_ai_move_cached(board_tuple: tuple, valid_moves: tuple) -> int:
    """
    Internal cached function that gets a move from the AI.
    Accepts a hashable tuple representation of the board.
    """
    if client is None:
        return -1 # Return error if client wasn't initialized
    try:
        # Convert the board tuple to a simple string format for the prompt.
        board_string = "\n".join([" ".join(map(str, row)) for row in board_tuple])

        prompt = f"""
        You are an expert Connect 4 player. It is your turn to play as Yellow (2).
        The current board state is below (0=empty, 1=Red, 2=Yellow).
        The board has 6 rows and 7 columns.

        Board:
        {board_string}

        The available columns are: {valid_moves}.
        Which column do you choose? Your answer must be only a single number from the list of available columns.
        """
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a Connect 4 expert that only responds with a single number."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        response_content = response.choices[0].message.content
        
        # --- Robustness Check ---
        # 1. Try to convert the AI's response to an integer.
        # 2. Check if the chosen column is in the list of valid moves.
        try:
            chosen_col = int(response_content.strip())
            if chosen_col in valid_moves:
                return chosen_col
        except ValueError:
            # The AI returned non-numeric text.
            print(f"AI returned an invalid (non-numeric) response: '{response_content}'")

        # --- Safeguard ---
        # If the AI's response was invalid or not in the valid_moves list, pick a random valid move.
        print("AI response was invalid. Picking a random valid move as a fallback.")
        return np.random.choice(list(valid_moves))

    except Exception as e:
        print(f"An error occurred while getting the AI move: {e}")
        # If the API call fails entirely, fall back to a random valid move.
        return np.random.choice(list(valid_moves))
