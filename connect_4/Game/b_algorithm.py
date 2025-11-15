"""
This module contains tracking matrices intended for use in dynamically tracking the gameplay as well as tracking each player's scorecard. 
It is an implementation intended to facilitate the incorporation of Agentic AI algorithms for Connect 4.
"""
import numpy as np
from .constants import ROWS, COLS
from typing import Tuple
# Define constants for gameplay matrix values"
PLAYER_RED = 1
PLAYER_YELLOW = 2


# create_tracking_matrices function returns three separate NumPy arrays (the tracking matrices) grouped together in a single tuple.
def create_tracking_matrices() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Creates and returns three tracking matrices:
    1. Gameplay Matrix: Tracks the state of the game board.
    2. Red Scorecard Matrix: Tracks Red player's scorecard.
    3. Yellow Scorecard Matrix: Tracks Yellow player's scorecard.
    
    Each matrix is initialized to zeros.
    """
    # gameplay: Represents player pieces. 1 for Red, 2 for Yellow.
    gameplay = np.zeros((ROWS, COLS), dtype=np.int8)
    # red_scorecard: Records 1 at any position a red piece is played.
    red_scorecard = np.zeros((ROWS, COLS), dtype=np.int8)
    # yellow_scorecard: Records 1 at any position a yellow piece is played.
    yellow_scorecard = np.zeros((ROWS, COLS), dtype=np.int8)
    
    return gameplay, red_scorecard, yellow_scorecard
