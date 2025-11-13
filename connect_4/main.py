import pygame
from pygame.locals import *
from Game.constants import WIDTH, HEIGHT, FPS, RED, YELLOW
from Game.board import Board


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4")

    run = True
    clock = pygame.time.Clock()
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


if __name__ == "__main__":
    main()
