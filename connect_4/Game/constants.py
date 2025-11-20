"""
This module defines constants used in the Connect 4 game, including dimensions, colors, and frame rate. 
"""
import pygame
 
WIDTH, HEIGHT = 800, 700
 # rows and columns are set to the standard Connect 4 dimensions and the requirements for the assessment
ROWS, COLS = 6, 7
COLUMN_SIZE = 600 // COLS 
# Divides 600px(the width less the area architected for the info section) by number of columns in order to calculate column size 
ROW_SIZE = (HEIGHT - 200) // ROWS 
#Row size, subtracts 200px to account for info section
TOKEN_RADIUS = 20
# The radius of each game piece
FPS = 60
CIRCLE_SIZE = (40, 40)
# Size of each piece when drawn on the board

# Button dimensions and positions
BUTTON_WIDTH = 160
BUTTON_HEIGHT = 50
BUTTON_PADDING = 20
BUTTON_X = 600 + (200 - BUTTON_WIDTH) // 2 # Center in info_section

# Button Colors
BUTTON_COLOR = (65,105,225) # Royal Blue
BUTTON_HOVER_COLOR = (100,149,237) # Cornflower Blue
BUTTON_TEXT_COLOR = (255, 255, 255)


# RGB COLORS
RED = (255, 0, 0)
YELLOW = (255, 255, 0) 
BLUE = (65,105,225)
SKY_BLUE = (128,128,0)
WHITE = (255, 255, 255)

# Define constants for gameplay matrix values"
PLAYER_RED = 1
PLAYER_YELLOW = 2