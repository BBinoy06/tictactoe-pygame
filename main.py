import pygame
import sys

pygame.init()

screen = pygame.display.set_mode(size=(500, 500))
pygame.display.set_caption("Tic-Tac-Toe")
running = True
BLACK = (0, 0, 0)

def drawGrid():
    blockSize = 100
    for x in range(0, 500, blockSize):
        for y in range(0, 500, blockSize):
            square = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, square, 1)

while running:
    screen.fill("grey")
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    

pygame.quit()

    
    
