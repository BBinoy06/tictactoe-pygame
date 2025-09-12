import pygame
import sys

pygame.init()

WINDOW_SIZE = 600
BOARD_SIZE = 540
CELL_SIZE = 180

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic Tac Toe")
running = True

# images
easy_img = pygame.image.load("EasyBtn.png").convert_alpha()
hard_img = pygame.image.load("HardBtn.png").convert_alpha()
impossible_img = pygame.image.load("ImpossibleBtn.png").convert_alpha()

# change the size of buttons
easy_img = pygame.transform.scale(easy_img, (150, 60))
hard_img = pygame.transform.scale(hard_img, (150, 60))
impossible_img = pygame.transform.scale(impossible_img, (150, 60))

# positions
easy_rect = easy_img.get_rect(topleft=(225, 200))
hard_rect = hard_img.get_rect(topleft=(225, 300))
impossible_rect = impossible_img.get_rect(topleft=(225, 400))

# colours
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

xboard = (WINDOW_SIZE - BOARD_SIZE) // 2
yboard = (WINDOW_SIZE - BOARD_SIZE) // 2

def MenuButton():
    while True:
        screen.fill(GREY)
        screen.blit(easy_img, easy_rect)
        screen.blit(hard_img, hard_rect)
        screen.blit(impossible_img, impossible_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                if easy_rect.collidepoint(event.pos):
                    return "easy"
                elif hard_rect.collidepoint(event.pos):
                    return "hard"
                elif impossible_rect.collidepoint(event.pos):
                    return "impossible"

def drawGrid():
    pygame.draw.rect(screen, GREY, (xboard, yboard, BOARD_SIZE, BOARD_SIZE))

    for i in range (1,3):
        pygame.draw.line(screen, BLACK, (xboard, yboard + i * CELL_SIZE), (xboard + BOARD_SIZE, yboard + i * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (xboard + i * CELL_SIZE, yboard), (xboard + i * CELL_SIZE, yboard + BOARD_SIZE), 5)

difficulty = MenuButton()
print("User selected:", difficulty)

running = True

while running:
    
    screen.fill(GREY)
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    

pygame.quit()

    
    
