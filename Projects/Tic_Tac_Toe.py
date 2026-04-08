import random
import pygame


pygame.init()


FPS = 64
WIDTH, HEIGHT = 400, 400
game_width, game_height = 300, 300
pyclock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X-O Game")

board = ["" for _ in range(9)]

def draw_lines():
    font = pygame.font.SysFont("Algerian", 20)
    text = font.render("Remeber: First Turn == ", True, "Green")
    x_text = font.render("\"X\"", True, "Blue")
    screen.blit(text, (50, 5))
    screen.blit(x_text, (290, 5))
    Rect = pygame.draw.rect(screen,"White" , (50, 50 , 300, 300), 0)
    
    pygame.draw.line(screen, "Black", (50, 50), (50, 350), 4)
    pygame.draw.line(screen, "Black", (350, 50), (350, 350), 4)
    pygame.draw.line(screen, "Black", (50, 50), (350, 50), 4)
    pygame.draw.line(screen, "Black", (50, 350), (350, 350), 4)

    pygame.draw.line(screen, "Blue", (150, 50), (150, 350), 2)
    pygame.draw.line(screen, "Blue", (250, 50), (250, 350), 2)
    pygame.draw.line(screen, "Blue", (50, 150), (350, 150), 2)
    pygame.draw.line(screen, "Blue", (50, 250), (350, 250), 2)

def game_screen():
    turn = "X"
    global board
    screen.fill("Grey")
    draw_lines()
    font = pygame.font.SysFont("algerian", 44)
    x_text = font.render("X", True, ("Red"))
    o_text = font.render("O", True, ("Green"))
    win_font = pygame.font.SysFont("algerian", 36)

    key_pos = {
        pygame.K_KP7 : (0, 0),
        pygame.K_KP8 : (1, 0),
        pygame.K_KP9 : (2, 0),
        pygame.K_KP4 : (0, 1),
        pygame.K_KP5 : (1, 1),
        pygame.K_KP6 : (2, 1),
        pygame.K_KP1 : (0, 2),
        pygame.K_KP2 : (1, 2),
        pygame.K_KP3 : (2, 2),
    }

    box1 = pygame.Rect(75, 75, 100, 100)
    box2 = pygame.Rect(175, 75, 100, 100)
    box3 = pygame.Rect(275, 75, 100, 100)
    box4 = pygame.Rect(75, 175, 100, 100)
    box5 = pygame.Rect(175, 175, 100, 100)
    box6 = pygame.Rect(275, 175, 100, 100)
    box7 = pygame.Rect(75, 275, 100, 100)
    box8 = pygame.Rect(175, 275, 100, 100)
    box9 = pygame.Rect(275, 275, 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if turn == "X":
                    if event.key == pygame.K_KP1 and board[0] == "":
                        screen.blit(x_text, box1)
                        board[0] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP2 and board[1] == "":
                        screen.blit(x_text, box2)
                        board[1] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP3 and board[2] == "":
                        screen.blit(x_text, box3)
                        board[2] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP4 and board[3] == "":
                        screen.blit(x_text, box4)
                        board[3] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP5 and board[4] == "":
                        screen.blit(x_text, box5)
                        board[4] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP6 and board[5] == "":
                        screen.blit(x_text, box6)
                        board[5] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP7 and board[6] == "":
                        screen.blit(x_text, box7)
                        board[6] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP8 and board[7] == "":
                        screen.blit(x_text, box8)
                        board[7] = "X"
                        turn = "O"
                    elif event.key == pygame.K_KP9 and board[8] == "":
                        screen.blit(x_text, box9)
                        board[8] = "X"
                        turn = "O"
                if turn == "O":
                    if event.key == pygame.K_KP1 and board[0] == "":
                        screen.blit(o_text, box1)
                        board[0] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP2 and board[1] == "":
                        screen.blit(o_text, box2)
                        board[1] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP3 and board[2] == "":
                        screen.blit(o_text, box3)
                        board[2] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP4 and board[3] == "":
                        screen.blit(o_text, box4)
                        board[3] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP5 and board[4] == "":
                        screen.blit(o_text, box5)
                        board[4] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP6 and board[5] == "":
                        screen.blit(o_text, box6)
                        board[5] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP7 and board[6] == "":
                        screen.blit(o_text, box7)
                        board[6] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP8 and board[7] == "":
                        screen.blit(o_text, box8)
                        board[7] = "O"
                        turn = "X"
                    elif event.key == pygame.K_KP9 and board[8] == "":
                        screen.blit(o_text, box9)
                        board[8] = "O"
                        turn = "X"
                result = winner()

                if result:
                    if result == "Draw":
                        end_text = win_font.render("Its a Tie!", True, "Blue")
                    else:
                        end_text = win_font.render(f"{result} Wins!!", True, "Blue")
                    screen.blit(end_text, (100, 200))
                    
                    
                    
            pygame.display.update()
            pyclock.tick(FPS)

def winner():
    global board
    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    
    for a, b, c in win_combinations:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a]  
    
    if "" not in board:
        return "Draw"
    
    return None


    
    
    
if __name__ == "__main__":
    game_screen()    
    