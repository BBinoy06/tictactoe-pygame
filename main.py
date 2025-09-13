import pygame
import sys
import random


class Computer:
    def __init__(self, mark, difficulty="easy"):
        self.mark = mark
        self.difficulty = difficulty
        self.opponent = "X" if self.mark == "O" else "O"

    def evaluate(self, board, noMoves):
        winner = board.check_win()
        if winner == self.mark:
            return 10 - noMoves
        elif winner == self.opponent:
            return -10 + noMoves
        return 0

    def minimax(self, board, noMoves, MaxOrMin):
        score = self.evaluate(board, noMoves)
        if score != 0:
            return score
        if board.is_full():
            return 0

        if MaxOrMin:
            best = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board.grid[r][c] == " ":
                        board.grid[r][c] = self.mark
                        val = self.minimax(board, noMoves + 1, False)
                        board.grid[r][c] = " "
                        best = max(best, val)
            return best
        else:
            best = float('inf')
            for r in range(3):
                for c in range(3):
                    if board.grid[r][c] == " ":
                        board.grid[r][c] = self.opponent
                        val = self.minimax(board, noMoves + 1, True)
                        board.grid[r][c] = " "
                        best = min(best, val)
            return best

    def find_best_move(self, board):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == " "]
        best_score = -float('inf')
        best_moves = []

        for r, c in empty_cells:
            board.grid[r][c] = self.mark
            score = self.minimax(board, 0, False)
            board.grid[r][c] = " "

            if score > best_score:
                best_score = score
                best_moves = [(r, c)]
            elif score == best_score:
                best_moves.append((r, c))

        return random.choice(best_moves) if best_moves else random.choice(empty_cells)

    def get_move(self, board):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == " "]

        if self.difficulty == "easy":
            return random.choice(empty_cells)

        if self.difficulty == "medium":
            
            for (r, c) in empty_cells:
                board.grid[r][c] = self.mark
                if board.check_win() == self.mark:
                    board.grid[r][c] = " "
                    return r, c
                board.grid[r][c] = " "

            
            for (r, c) in empty_cells:
                board.grid[r][c] = self.opponent
                if board.check_win() == self.opponent:
                    board.grid[r][c] = " "
                    return r, c
                board.grid[r][c] = " "

            return random.choice(empty_cells)

        if self.difficulty == "hard":
            return self.find_best_move(board)

class BoardWrapper:
    def __init__(self, grid):
        self.grid = grid

    def check_win(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]
        return None

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False
        return True

pygame.init()

WINDOW_SIZE = 700
BOARD_SIZE = 540
CELL_SIZE = 180

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Images
easy_img = pygame.image.load("EasyBtn.png").convert_alpha()
hard_img = pygame.image.load("HardBtn.png").convert_alpha()
impossible_img = pygame.image.load("ImpossibleBtn.png").convert_alpha()
home_img = pygame.image.load("HomeButton.png").convert_alpha()


easy_img = pygame.transform.scale(easy_img, (180, 80))
hard_img = pygame.transform.scale(hard_img, (180, 80))
impossible_img = pygame.transform.scale(impossible_img, (180, 80))
home_img = pygame.transform.scale(home_img, (30, 30))


easy_rect = easy_img.get_rect(topleft=(225, 200))
hard_rect = hard_img.get_rect(topleft=(225, 300))
impossible_rect = impossible_img.get_rect(topleft=(225, 400))
home_rect = home_img.get_rect(topright=(WINDOW_SIZE - 30, 30))


BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

xboard = (WINDOW_SIZE - BOARD_SIZE) // 2
yboard = (WINDOW_SIZE - BOARD_SIZE) // 2

gap = 10

restart_img = pygame.image.load("RestartBtn.png").convert_alpha()
restart_img = pygame.transform.scale(restart_img, (30, 30))
restart_rect = restart_img.get_rect(topright=(home_rect.left - gap, home_rect.top))

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
                    return "medium"
                elif impossible_rect.collidepoint(event.pos):
                    return "hard"

def drawGrid():
    pygame.draw.rect(screen, GREY, (xboard, yboard, BOARD_SIZE, BOARD_SIZE))
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (xboard, yboard + i * CELL_SIZE), (xboard + BOARD_SIZE, yboard + i * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (xboard + i * CELL_SIZE, yboard), (xboard + i * CELL_SIZE, yboard + BOARD_SIZE), 5)

def draw_mark(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED,
                    (xboard + c*CELL_SIZE + 20, yboard + r*CELL_SIZE + 20),
                    (xboard + (c+1)*CELL_SIZE - 20, yboard + (r+1)*CELL_SIZE - 20), 10)
                pygame.draw.line(screen, RED,
                    (xboard + (c+1)*CELL_SIZE - 20, yboard + r*CELL_SIZE + 20),
                    (xboard + c*CELL_SIZE + 20, yboard + (r+1)*CELL_SIZE - 20), 10)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE,
                    (xboard + c*CELL_SIZE + CELL_SIZE//2, yboard + r*CELL_SIZE + CELL_SIZE//2),
                    CELL_SIZE//2 - 20, 10)
    

def computer_move():
    wrapper = BoardWrapper(board)
    row, col = computer.get_move(wrapper)
    board[row][col] = "O"

def game_over_result():
    wrapper = BoardWrapper(board)
    winner = wrapper.check_win()
    if winner:
        return winner 
    elif wrapper.is_full():
        return "Draw"
    return None


current_screen = "menu"
difficulty = None
computer = None
game_over = False
winner_text = ""

while True:
    screen.fill(GREY)

    if current_screen == "menu":
        difficulty = MenuButton()
        print("User selected:", difficulty)

        
        computer = Computer("O", difficulty)

        current_screen = "grid"
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False
        winner_text = ""

    elif current_screen == "grid":
        drawGrid()
        draw_mark(board)
        screen.blit(home_img, home_rect)
        screen.blit(restart_img, restart_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if home_rect.collidepoint(event.pos):
                    current_screen = "menu"
                    game_over = False
                    winner_text = ""

                if restart_rect.collidepoint(event.pos):
                    board = [[" " for _ in range(3)] for _ in range(3)]
                    current_player = "X"
                    game_over = False
                    winner_text = ""
                elif not game_over:
                    x, y = event.pos
                    col = (x - xboard) // CELL_SIZE
                    row = (y - yboard) // CELL_SIZE

                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                        board[row][col] = "X"

                        wrapper = BoardWrapper(board)
                        winner = wrapper.check_win()
                        if winner:
                            game_over = True
                            winner_text = "You won!" if winner == "X" else "You lost!"
                        elif wrapper.is_full():
                            game_over = True
                            winner_text = "Draw!"
                        else:
                            
                            row_c, col_c = computer.get_move(wrapper)
                            board[row_c][col_c] = "O"

                            winner = wrapper.check_win()
                            if winner:
                                game_over = True
                                winner_text = "You won!" if winner == "X" else "You lost!"
                            elif wrapper.is_full():
                                game_over = True
                                winner_text = "Draw!"

        
        if game_over:
            font = pygame.font.SysFont(None, 50)
            overlay_rect = pygame.Rect(xboard, yboard + BOARD_SIZE + 10, BOARD_SIZE, 60)
            pygame.draw.rect(screen, GREY, overlay_rect)
            pygame.draw.rect(screen, PURPLE, overlay_rect, 3)
            text_surface = font.render(winner_text, True, PURPLE)
            text_rect = text_surface.get_rect(center=overlay_rect.center)
            screen.blit(text_surface, text_rect)

    pygame.display.flip()
