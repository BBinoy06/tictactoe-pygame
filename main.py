import pygame
import sys

pygame.init()

screen = pygame.display.set_mode(size=(500, 500))
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

    pygame.display.flip()
    

pygame.quit()

    
    
