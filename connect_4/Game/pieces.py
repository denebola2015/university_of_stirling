"""This module defines the Piece classes for the Connect 4 game, including RedPiece and YellowPiece. It gets and sets the color of each piece 
and provides string representations for debugging purposes.  """

import pygame
from .constants import RED, YELLOW

class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color       
    
    def set_color(self, color):
        self.color = color


# This code defines RedPiece and YellowPiece class which both inherit from the more general Piece class above.
class RedPiece(Piece):
    def __init__(self):
        super().__init__(RED) # super().__init__(RED) calls the parent's __init__ method and passes it the RED 

    def __repr__(self):
        return f"RedPiece(color={self.color})" # string representation of the object

    def __str__(self):
        return f"RedPiece(color={self.color})" # Another string representation of the object

class YellowPiece(Piece):
    def __init__(self):
        super().__init__(YELLOW)    

    def __repr__(self):
        return f"YellowPiece(color={self.color})"

    def __str__(self):
        return f"YellowPiece(color={self.color})"