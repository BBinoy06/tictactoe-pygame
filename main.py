import pygame
import sys
import random

pygame.init()

WINDOW_SIZE = 600
BOARD_SIZE = 540
CELL_SIZE = 180

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic Tac Toe")
running = True

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"


# images
easy_img = pygame.image.load("EasyBtn.png").convert_alpha()
hard_img = pygame.image.load("HardBtn.png").convert_alpha()
impossible_img = pygame.image.load("ImpossibleBtn.png").convert_alpha()
home_img = pygame.image.load("HomeButton.png").convert_alpha()

# change the size of buttons
easy_img = pygame.transform.scale(easy_img, (150, 60))
hard_img = pygame.transform.scale(hard_img, (150, 60))
impossible_img = pygame.transform.scale(impossible_img, (150, 60))
home_img = pygame.transform.scale(home_img, (20, 20))

# positions
easy_rect = easy_img.get_rect(topleft=(225, 200))
hard_rect = hard_img.get_rect(topleft=(225, 300))
impossible_rect = impossible_img.get_rect(topleft=(225, 400))
home_rect = home_img.get_rect(topright=(WINDOW_SIZE - 30, 30))

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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

def draw_mark(board):
    if current_screen == "grid":
        for r in range(3):
            for c in range(3):
                if board[r][c] == "X":
                    pygame.draw.line(screen, BLACK,
                        (xboard + c*CELL_SIZE + 20, yboard + r*CELL_SIZE + 20),
                        (xboard + (c+1)*CELL_SIZE - 20, yboard + (r+1)*CELL_SIZE - 20), 10)
                    pygame.draw.line(screen, BLACK,
                        (xboard + (c+1)*CELL_SIZE - 20, yboard + r*CELL_SIZE + 20),
                        (xboard + c*CELL_SIZE + 20, yboard + (r+1)*CELL_SIZE - 20), 10)
                elif board[r][c] == "O":
                    pygame.draw.circle(screen, BLACK,
                        (xboard + c*CELL_SIZE + CELL_SIZE//2, yboard + r*CELL_SIZE + CELL_SIZE//2),
                        CELL_SIZE//2 - 20, 10)

def computer_move(difficulty):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if difficulty == "easy":
        if empty_cells:
            row, col = random.choice(empty_cells)
            board[row][col] = "O"
            

def switch_turn(turn):
    if turn == "player":
        return "computer"
    else:
        return "player"
    
def check_win(board):
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]            

        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]

        return None

def is_full():
        for row in board:
            for cell in row:
                if cell == " ":
                    return False
        return True

def is_over():
        if check_win() is not None:
            return True
        if is_full():
            return True
        return False

        
    

current_screen = "menu"
difficulty = None

while True:
    screen.fill(GREY)

    if current_screen == "menu":
        difficulty = MenuButton()
        print("User selected:", difficulty)
        current_screen = "grid"
        
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

    elif current_screen == "grid":
        drawGrid()
        draw_mark(board)
        screen.blit(home_img, home_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type ==pygame.MOUSEBUTTONDOWN and event.button == 1:
                if home_rect.collidepoint(event.pos):
                    current_screen = "menu"
                else:
                    x, y = event.pos
                    col = (x - xboard)// CELL_SIZE
                    row =(y - yboard)// CELL_SIZE
                    if 0 <=row < 3 and 0 <= col < 3:
                        if board[row][col] == " " and current_player == "X":
                            board[row][col] = "X"

                            if check_win(board) == "X":
                                print("Player wins!")
                                current_screen = "menu"
                            elif is_full():
                                print("It's a draw!")
                                current_screen = "menu"
                            else:

                                computer_move(difficulty)
                                if check_win(board) == "O":
                                    print("Computer wins!")
                                    current_screen = "menu"
                                elif is_full():
                                    print("It's a draw!")
                                    current_screen = "menu"

                
                if difficulty == "easy":
                    computer_move(difficulty)
                    current_player = "X"

    pygame.display.flip()
