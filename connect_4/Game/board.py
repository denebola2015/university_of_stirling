import pygame
from .constants import BLUE, WHITE, SKY_BLUE, ROWS, COLS, COLUMN_SIZE, ROW_SIZE, HEIGHT, TOKEN_RADIUS, WIDTH, CIRCLE_SIZE


class Board:
    def __init__(self):
        # initialize an empty board (None for empty slots)
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def draw_board(self, win):
        # Draw the first section (game board area)
        game_section = pygame.Rect(0, 0, 600, HEIGHT)
        pygame.draw.rect(win, BLUE, game_section)

        # Draw the second section (blank area)
        info_section = pygame.Rect(600, 0, 200, HEIGHT)
        pygame.draw.rect(win, SKY_BLUE, info_section)

        for row in range(ROWS):
            for col in range(COLS):
                x = col * COLUMN_SIZE + COLUMN_SIZE // 2
                y = row * ROW_SIZE + ROW_SIZE // 2
                center = (x, y)
                radius = TOKEN_RADIUS
                pygame.draw.circle(win, WHITE, center, radius)
