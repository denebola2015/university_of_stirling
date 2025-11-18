""" This module provides a function to get the AI's suggested move in the Connect 4 game. It Sends the current 'gameplay' matrix 
to both OpenAI's GPT model and DeepSeek's API and - depending on successful connection to anyone of these, returns the AI's suggested move. 
Both the 'OPENAI_API_KEY' and 'DEEPSEEK_API_KEY' environment variable are set locally on my computer. Any porting of this code to another environment
will require setting up an OpenAI API key or DeepSeek API key in the environment variables for the code to function correctly.
The gameplay_matrix is a numpy array representing the Connect 4 board.
                         0 = empty, 1 = Red (player), 2 = Yellow (AI).
"""
import os
from openai import OpenAI
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
def get_ai_move(gameplay_matrix: np.ndarray) -> int:
    """Gets a move from the AI. Returns an integer for the column (0-6) or -1 on error."""
    if client is None:
        return -1 # Return error if client wasn't initialized
    try:
        # Convert the numpy matrix to a simple string format for the prompt.
        board_string = "\n".join([" ".join(map(str, row)) for row in gameplay_matrix])

        prompt = f"""
        You are an expert Connect 4 player. It is your turn to play as Yellow (2).
        The current board state is below (0=empty, 1=Red, 2=Yellow).
        The board has 6 rows and 7 columns.

        Board:
        {board_string}

        Which column (0-6) do you choose? Your answer must be only a single number from 0 to 6.
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
        
        # Convert the response to an integer.
        return int(response_content)

    except Exception as e:
        print(f"An error occurred while getting the AI move: {e}")
        return -1 # Return -1 to indicate an error.
