"""
This module defines the Piece class for the Connect 4 game. It handles the color and drawing of a game piece.
"""

import pygame
from .constants import TOKEN_RADIUS

class Piece:
    def __init__(self, color):
        self.color = color

    def draw(self, win, x, y):
        """Draws the piece on the window."""
        pygame.draw.circle(win, self.color, (x, y), TOKEN_RADIUS)
        
class RedPiece(Piece):
    pass
class YellowPiece(Piece):
    pass