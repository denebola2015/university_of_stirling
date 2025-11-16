"""
This module defines the Board class for the Connect 4 game, it handles the drawing of the game board and the placement of pieces. 
It also initializes the tracking matrices used for gameplay and scorecard tracking.
"""

import pygame
from .constants import BLUE, WHITE, SKY_BLUE, ROWS, COLS, COLUMN_SIZE, ROW_SIZE, HEIGHT, TOKEN_RADIUS, WIDTH, CIRCLE_SIZE, RED, YELLOW
from .pieces import Piece
from .test import check_win_vectorized # Import the new function
from .b_algorithm import create_tracking_matrices

class Board:

    def __init__(self):
        # initialize an empty board 
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        # Initialize the tracking matrices from your algorithm file
        self.gameplay, self.red_scorecard, self.yellow_scorecard = create_tracking_matrices() 

    def drop_piece(self, col, piece_color):
        """
        Drops a piece of a given color into the specified column.
        Returns the (row, col) of the move if successful, otherwise None.
        """
        for r in range(ROWS - 1, -1, -1):  # Iterate from the bottom row up
            if self.board[r][col] is None:
                self.board[r][col] = Piece(piece_color)
                # Assign 
                # Update the tracking matrices
                if piece_color == RED:
                    self.gameplay[r][col] = 1
                    self.red_scorecard[r][col] = 1 
                    # If a red piece is played, record 1 at that position in the red_scorecard matrix and 1 in the gameplay matrix
                else: # Yellow piece
                    self.gameplay[r][col] = 2
                    self.yellow_scorecard[r][col] = 1
                    # If a yellow piece is played, record 1 at that position in the yellow_scorecard matrix and 2 in the gameplay matrix

                return r, col  # Return the position of the new piece
        return None  # Indicates the column is full

    def check_win(self, row, col):
        """Checks for a win from the last piece dropped."""
        player_id = self.gameplay[row][col]
        if player_id == 0:
            return None
        
        # Select the correct scorecard based on the player
        scorecard = self.red_scorecard if player_id == 1 else self.yellow_scorecard
        
        # Use the new vectorized win check algorithm
        if check_win_vectorized(scorecard, row, col):
            return player_id # Return the winning player's ID
        
        return None # No winner

    def draw_board(self, win):
        # Board is divided into two regions. One containing the game section, the other containing an info section that contains information from tracking Matrices as well as operational buttons
        # Draw the first section (game board area)
        game_section = pygame.Rect(0, 0, 600, HEIGHT)
        pygame.draw.rect(win, BLUE, game_section)

        # Draw the second section (info section)
        info_section = pygame.Rect(600, 0, 200, HEIGHT)
        pygame.draw.rect(win, SKY_BLUE, info_section)

        for row in range(ROWS):
            for col in range(COLS):
                # Calculate the center of the circle dynamically
                x = int(col * COLUMN_SIZE + COLUMN_SIZE / 2)
                y = int(row * ROW_SIZE + ROW_SIZE / 2)
                
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(win, x, y)
                else:
                    # Draw an empty slot
                    pygame.draw.circle(win, WHITE, (x, y), TOKEN_RADIUS)
