import pygame
from Game.constants import WIDTH, HEIGHT
from Game.board import Board

FPS = 120
# Set display mode and caption for window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Set event loop
def main():
    run = True
    clock = pygame.time.Clock(FPS)
    board = Board()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"Mouse clicked at position: {pos}")  
                
                
                
        board.draw_board(WIN)
        pygame.display.update()  
          
    pygame.quit()


        


# if __name__ == "__main__":  
main()
