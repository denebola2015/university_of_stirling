"""
This module provides a vectorized win-checking algorithm for Connect 4.
The algorithm leverages NumPy for highly efficient, vectorized checks
with early-exit logic.
"""
import numpy as np

def check_win_vectorized(scorecard: np.ndarray, row: int, col: int) -> bool:
    """
    Checks for a win on the player's scorecard from the last piece dropped at (row, col)
    using explicit slicing and broadcasting for consecutive checks.

    Args:
        scorecard: The player's scorecard matrix (red_scorecard or yellow_scorecard).
        row: The row of the last piece dropped.
        col: The column of the last piece dropped.
    """
    if scorecard[row, col] == 0:
        return False

    ROWS, COLS = scorecard.shape
    player_val = 1 # In a scorecard, the player's piece is always 1

    # --- Horizontal Check ---
    current_row_line = scorecard[row, :]
    if np.any(
        (current_row_line[:-3] == player_val) &
        (current_row_line[1:-2] == player_val) &
        (current_row_line[2:-1] == player_val) &
        (current_row_line[3:] == player_val)
    ):
        return True

    # --- Vertical Check ---
    if row <= ROWS - 4:
        vertical_slice = scorecard[row:row+4, col]
        if np.all(vertical_slice == player_val):
            return True

    # --- Main Diagonal Check (\) ---
    main_diag_line = np.diagonal(scorecard, offset=col - row)
    if len(main_diag_line) >= 4 and np.any(
        (main_diag_line[:-3] == player_val) &
        (main_diag_line[1:-2] == player_val) &
        (main_diag_line[2:-1] == player_val) &
        (main_diag_line[3:] == player_val)
    ):
        return True

    # --- Anti-Diagonal Check (/) ---
    anti_diag_line = np.diagonal(np.fliplr(scorecard), offset=(COLS - 1 - col) - row)
    if len(anti_diag_line) >= 4 and np.any(
        (anti_diag_line[:-3] == player_val) &
        (anti_diag_line[1:-2] == player_val) &
        (anti_diag_line[2:-1] == player_val) &
        (anti_diag_line[3:] == player_val)
    ):
        return True

    return False