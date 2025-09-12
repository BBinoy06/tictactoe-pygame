import pygame
import sys

pygame.init()

WINDOW_SIZE = 600
BOARD_SIZE = 540
CELL_SIZE = 300

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic Tac Toe")
running = True

# colours
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

xboard = (WINDOW_SIZE - BOARD_SIZE) // 2
yboard = (WINDOW_SIZE - BOARD_SIZE) // 2

def drawGrid():
    square_board = pygame.Rect(xboard, yboard, BOARD_SIZE, BOARD_SIZE)
    pygame.draw.rect(screen, GREY, square_board)
    

while running:
    screen.fill(GREY)
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    

pygame.quit()

    
    
