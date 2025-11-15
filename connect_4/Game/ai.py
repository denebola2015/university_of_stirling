""" This module provides a function to get the AI's suggested move in the Connect 4 game. It Sends the current 'gameplay' matrix 
to OpenAI's GPT model through the "deepseek" API and returns the AI's suggested move. The OpenAI client automatically uses the 'DEEPSEEK_API_KEY' environment variable.
The gameplay_matrix is a numpy array representing the Connect 4 board.
                         0 = empty, 1 = Red (player), 2 = Yellow (AI).
"""
import os
from openai import OpenAI
import numpy as np

def get_ai_move(gameplay_matrix: np.ndarray) -> int: # Returns: An integer representing the column (0-6) the AI wants to play in.
   
    try:
        # The client automatically reads the API key from the OPENAI_API_KEY environment variable.
        client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")


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

        """chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a Connect 4 expert that only responds with a single number."},
                {"role": "user", "content": prompt},
            ],
            model="gpt-4o",
            max_tokens=5, # A small number is sufficient for a single-digit response.
        )"""
        
        response_content = response.choices[0].message.content
        
        # Convert the response to an integer.
        return int(response_content)

    except Exception as e:
        print(f"An error occurred while getting the AI move: {e}")
        return -1 # Return -1 to indicate an error.
