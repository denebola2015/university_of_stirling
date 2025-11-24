"""
Main module to run the Connect 4 game using Pygame. It initializes the game window, handles user input, updates the game state, 
and displays the game board along with tracking matrices for gameplay and scorecards.
"""

import pygame
import numpy as np
from Game.constants import WIDTH, HEIGHT, FPS, RED, YELLOW, COLUMN_SIZE, BUTTON_X, BUTTON_HEIGHT, BUTTON_PADDING, COLS
from Game.board import Board 
from Game.buttons import Button, draw_matrix_info
from Game.ai import get_ai_move 
from Game.ai import get_ai_move



def reset_game():
    """Resets the game to its initial state."""
    board = Board()
    turn = RED
    game_over = False
    winner_text = ""
    return board, turn, game_over, winner_text

def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4")
    font = pygame.font.SysFont('monospace', 15, bold=True) 
    button_font = pygame.font.SysFont('comicsansms', 20, bold=True)
    winner_font = pygame.font.SysFont('comicsansms', 50, bold=True)
    
    run = True
    clock = pygame.time.Clock()
    board = Board() # Initialize the game board by instantiating the Board class
    ai_opponent = False # Default to Player vs. Player mode
    board, turn, game_over, winner_text = reset_game() # winner_text is initialized here
    
    button_y = 500
    refresh_button = Button(BUTTON_X, button_y, "New Game")
    button_y += BUTTON_HEIGHT + BUTTON_PADDING
    ai_button = Button(BUTTON_X, button_y, "Play AI")
    button_y += BUTTON_HEIGHT + BUTTON_PADDING
    quit_button = Button(BUTTON_X, button_y, "Quit")
    
    buttons = [refresh_button, ai_button, quit_button]  


    try:
        while run:
            clock.tick(FPS) 
            
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                button.check_hover(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle button clicks
                    if refresh_button.is_clicked(event):
                        board, turn, game_over, winner_text = reset_game()
                        continue 

                    if ai_button.is_clicked(event):                
                        if ai_opponent == True:
                            ai_opponent = False
                        else:
                            ai_opponent = True
                        board, turn, game_over, winner_text = reset_game()
                        pygame.display.set_caption(f"Connect 4 - {'Player vs AI' if ai_opponent else 'Player vs Player'}")
                        continue

                    if quit_button.is_clicked(event):
                        run = False

                    # Handle piece drop for human players
                    if not game_over and (turn == RED or (turn == YELLOW and not ai_opponent)):
                        mouse_x = event.pos[0]
                        if mouse_x < 600: # Ensures the click is within the game board info_section area
                            col = mouse_x // COLUMN_SIZE
                            move = board.drop_piece(col, turn)
                            if move:
                                row, col = move
                                winner = board.check_win(row, col)
                                if winner:
                                    game_over = True
                                    winner_text = f"{'RED' if winner == 1 else 'YELLOW'} WINS!"
                                turn = YELLOW if turn == RED else RED # Switch turns

            
            # Handle AI turn automatically after player has moved
            if not game_over and turn == YELLOW and ai_opponent: # AI's turn
                # Determines which columns are not full.
                valid_moves = [c for c in range(COLS) if board.gameplay[0][c] == 0]
                col = get_ai_move(board.gameplay, valid_moves)
                if col != -1:
                    move = board.drop_piece(col, YELLOW)
                    if move:
                        row, col = move
                        winner = board.check_win(row, col)
                        if winner:
                            game_over = True
                            winner_text = "AI WINS!"
                        turn = RED
                
            
            # --- Drawing ---
            if board.chk:  # Only redraw if the board has changed
                board.draw_board(WIN)
                draw_matrix_info(WIN, board, font)
                board.chk = False  # Reset the flag after drawing
                for button in buttons:
                    button.draw(WIN, button_font)
                

            if game_over:
                text_surface = winner_font.render(winner_text, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                WIN.blit(text_surface, text_rect)

            pygame.display.update()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
