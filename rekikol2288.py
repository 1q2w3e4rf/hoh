import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
x_wins = 0
o_wins = 0
FONT = pygame.font.SysFont("Arial", 30)
board = [[None]*3 for _ in range(3)]
current_player = "X"
starting_player = "X"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-Нолики")
game_over = False
turn = 0

def draw_board():
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i*200, 0), (i*200, 600), 5)
        pygame.draw.line(screen, BLACK, (0, i*200), (600, i*200), 5)

def draw_symbol(row, col, symbol):
    if symbol == "X":
        pygame.draw.line(screen, RED, (col*200+50, row*200+50), (col*200+150, row*200+150), 10)
        pygame.draw.line(screen, RED, (col*200+150, row*200+50), (col*200+50, row*200+150), 10)
    elif symbol == "O":
        pygame.draw.circle(screen, GREEN, (col*200+100, row*200+100), 50, 10)

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    return None

def check_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    winner = check_win()
    if winner != None:
        return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row = event.pos[1] // 200
            col = event.pos[0] // 200
            if board[row][col] == None:
                board[row][col] = current_player
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

    draw_board()
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                draw_symbol(i, j, board[i][j])

    turn_text = FONT.render("Ходит: " + current_player, True, BLACK)
    screen.blit(turn_text, (WIDTH - 150, 10))

    winner = check_win()
    if winner != None and not game_over:
        game_over = True
        turn = pygame.time.get_ticks()
    if game_over:
        screen.fill(WHITE)
        if winner == "X":
            text = FONT.render("Победили крестики!", True, RED)
            current_player = "O"
        else:
            text = FONT.render("Победили нолики!", True, GREEN)
            current_player = "X"
        screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 15))
        if pygame.time.get_ticks() - turn > 2000:
            game_over = False
            if winner == "X":
                x_wins += 1
            else:
                o_wins += 1
            board = [[None]*3 for _ in range(3)]

    if check_full():
        screen.fill(WHITE)
        text = FONT.render("Ничья!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 15))
        pygame.display.flip()
        pygame.time.wait(2000)
        board = [[None]*3 for _ in range(3)]

    score_text = FONT.render(f"X: {x_wins} O: {o_wins}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()