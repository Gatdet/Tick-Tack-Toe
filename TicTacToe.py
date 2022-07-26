import pygame
import numpy as np

#   variable.ndim - tells the dimensions of a list
#   variable.shape - tells the number of rows and colums in array
"""   1 represent X and 2 represent O"""

pygame.init()

screen = pygame.display.set_mode((650,670))
screen.fill("#bebebe")

#Title/Icon
pygame.display.set_caption("Tick-Tack-Toe")
icon = pygame.image.load("Tic_tac_toe.svg.png")
pygame.display.set_icon(icon)

#board
board_rows = 3
board_cols = 3

board = np.zeros((board_rows,board_cols)) #creates a 2D array with number of rows and cols

def board_lines():
    pygame.draw.line(screen, "#23395d", (25, 200), (590, 200), 7)
    pygame.draw.line(screen, "#23395d", (25, 400), (590, 400), 7)
    pygame.draw.line(screen, "#23395d", (200, 25), (200, 590), 7)
    pygame.draw.line(screen, "#23395d", (400, 25), (400, 590), 7)

def mark_square(row,col,player):
    board[row][col] = player

def available_move(row, col):
    return board[row][col] == 0

def board_full():
    for row in range(0,board_rows):
        for col in range(0, board_cols):
            if board[row][col]==0 or o_win()== True or x_win()==True:
                return False

    return True

def x_win():
    if board[0][0] == 1 and board[0][1]==1 and board[0][2]==1: #First roW
        pygame.draw.line(screen, "#f7504a", (20, 100), (600, 100), width=14)
        return True
    elif board[1][0] == 1 and board[1][1]==1 and board[1][2]==1: #Second row
        pygame.draw.line(screen, "#f7504a", (20, 300), (600, 300), width=14)
        return True
    elif board[2][0] == 1 and board[2][1]==1 and board[2][2]==1: #Third row
        pygame.draw.line(screen, "#f7504a", (20, 500), (600, 500), width=14)
        return True
    elif board[0][0] == 1 and board[1][0]==1 and board[2][0]==1:
        pygame.draw.line(screen, "#f7504a", (110, 20), (110, 600), width=14)
        return True
    elif board[0][1] == 1 and board[1][1]==1 and board[2][1]==1:
        pygame.draw.line(screen, "#f7504a", (310, 20), (310, 600), width=14)
        return True
    elif board[0][2] == 1 and board[1][2]==1 and board[2][2]==1:
        pygame.draw.line(screen, "#f7504a", (510, 20), (510, 600), width=14)
        return True
    elif board[0][2] == 1 and board[1][1]==1 and board[2][0]==1:
        pygame.draw.line(screen, "#f7504a", (610, 0), (0, 610), width=14)
        return True
    elif board[0][0] == 1 and board[1][1]==1 and board[2][2]==1:
        pygame.draw.line(screen, "#f7504a", (0, 0), (600, 600), width=14)
        return True

    return False

def o_win():
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:  # First row
        pygame.draw.line(screen, "#03befc", (20, 100), (600, 100), width=14)
        return True
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:  # Second row
        pygame.draw.line(screen, "#03befc", (20, 300), (600, 300), width=14)
        return True
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:  # Third row
        pygame.draw.line(screen, "#03befc", (20, 500), (600, 500), width=14)
        return True
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2: #First col
        pygame.draw.line(screen, "#03befc", (110, 20), (110, 600), width=14)
        return True
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2: #Sec col
        pygame.draw.line(screen, "#03befc", (310, 20), (310, 600), width=14)
        return True
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2: #Third col
        pygame.draw.line(screen, "#03befc", (510, 20), (510, 600), width=14)
        return True
    elif board[0][2] == 2 and board[1][1]==2 and board[2][0]==2:
        pygame.draw.line(screen, "#03befc", (610, 0), (0, 610), width=14)
        return True
    elif board[0][0] == 2 and board[1][1]==2 and board[2][2]==2:
        pygame.draw.line(screen, "#03befc", (0, 0), (600, 600), width=14)
        return True
    return False

def game_restart():
    global game_active, board
    screen.fill("#bebebe")
    board = np.zeros((board_rows, board_cols))
    game_active = True

#Player X
x_turn = True
x_mark = pygame.image.load("x_mark.png")
x_win_count = 0
score_font = text_font = pygame.font.SysFont("Arial",50, True)
x_score = score_font.render(f"{x_win_count}", True, "#f7504a")
x_score_logo = pygame.image.load("small_x_mark.png")

#Player O
o_mark = pygame.image.load("o_mark.png")
o_score_logo = pygame.image.load("small_o_mark.png")
o_win_count = 0
o_score = score_font.render(f"{o_win_count}", True, "#03befc")


mouse_x = 0
mouse_y = 0
game_active = True
running  = True
while running:


    board_lines()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_active == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_restart()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] <=590 and event.pos[1]<=590:

                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    row_pressed = int(mouse_y//200)
                    cols_pressed = int(mouse_x//200)

                    if available_move(row_pressed,cols_pressed):
                        if x_turn:
                            screen.blit(x_mark, (int(cols_pressed *205 + 30), int(row_pressed *205 + 30)))
                            mark_square(row_pressed,cols_pressed, 1)
                            x_turn = False
                        else:
                            screen.blit(o_mark, (int(cols_pressed * 200 + 30), int(row_pressed * 200 + 30)))
                            mark_square(row_pressed, cols_pressed, 2)
                            x_turn = True
            screen.blit(x_score, (130,605))
            screen.blit(x_score_logo, (50, 610))
            screen.blit(o_score, (560,605))
            screen.blit(o_score_logo, (480, 605))
            if x_win():
                x_win_count+=1
                x_score = score_font.render(f"{x_win_count}", False, "#f7504a")
                game_active = False

            if o_win():
                o_win_count+=1
                o_score = score_font.render(f"{o_win_count}", True, "#03befc")
                x_turn = True
                game_active = False

    if board_full():
        game_active= False
        text_font = pygame.font.SysFont("Arial", 40, True)
        text = text_font.render("DRAW", False, "Black")
        screen.blit(text, (250,250))


    pygame.display.update()



