""" This module defines a Button class for creating interactive buttons in the Connect 4 game using Pygame.
It also includes a function to draw the gameplay and scorecard matrices on the game window.
"""
import pygame
from Game.constants import BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR 
from Game.board import Board 



class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y,BUTTON_WIDTH, BUTTON_HEIGHT)# Define a button class for future use
        self.text = text
        self.is_hovered = False
    
    
    def draw(self, win, font)
     current_color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
     pygame.draw.rect(win, current_color, self.rect, border_radius=12)
     text_surface = font.render(self.text, True, BUTTON_TEXT_COLOR)
     text_rect = text_surface.get_rect(center=self.rect.center)
     win.blit(text_surface, text_rect)
     
    def check_hover(self, mouse_pos):
         self.is_hovered = self.rect.collidepoint(mouse_pos)
         
         
    def is_clicked(self, event):
        return self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN
    
    
    
    def draw_matrix_info(win, board, font): 
    #Draws the gameplay and scorecard matrices on the game_section and info section of the window respectively.
        start_x = 610 
        start_y = 20
        line_height = 18
        black = (0, 0, 0)

        matrices = {
        "Gameplay": board.gameplay,
        "Red Scorecard": board.red_scorecard,
        "Yellow Scorecard": board.yellow_scorecard
    }

    y_offset = start_y # y_offset sets the starting vertical position for drawing text
    for title, matrix in matrices.items():
        # Draw title
        title_surface = font.render(title + ":", True, black)
        win.blit(title_surface, (start_x, y_offset))
        y_offset += line_height

        # Draw matrix rows
        for row in matrix:
            row_text = " ".join(map(str, row))
            text_surface = font.render(row_text, True, black)
            win.blit(text_surface, (start_x, y_offset))
            y_offset += line_height