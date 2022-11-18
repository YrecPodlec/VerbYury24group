import pygame
import sys
def win(massive_winner, znak):
    zero = 0
    for row in massive_winner:
        zero += row.count(0)
        if row.count(znak) == 6:
            return znak
    if zero == 0:
        return 'Ничья :/'
    return False
class GAME():
    block = 70
    otstyp = 20
    width = height = block * 6 + otstyp * 7
    window = (width, height)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("4 В РЯД!")
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    massive_winner = [[0] * 6 for i in range(6)]
    query = 0
    pygame.init()
    game_over = False
    swag = True
    while swag:
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (block + otstyp)
                    row = y_mouse // (block + otstyp)
                    if massive_winner[row][col] == 0:
                        if query % 2:
                            massive_winner[row][col] = 'Красный'
                        else:
                            massive_winner[row][col] = 'Зеленый'
                        query += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_over = False
                    query = 0
                    massive_winner = [[0] * 6 for i in range(6)]
                    screen.fill(black)
            except IndexError:
                pass
        if not game_over:
            for row in range(6):
                for col in range(6):
                    if massive_winner[row][col] == 'Красный':
                        color = red
                    elif massive_winner[row][col] == 'Зеленый':
                        color = green
                    else:
                        color = white
                    x = col * block + (col + 1) * otstyp
                    y = row * block + (row + 1) * otstyp
                    pygame.draw.rect(screen, color, (x, y, block, block))
        if (query % 6) == 0:
            game_over = win(massive_winner, 'Красный')
        else:
            game_over = win(massive_winner, 'Зеленый')
        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('monospace', 20)
            text_1 = font.render("ПОБЕДИЛ: " + game_over, True, white)
            text_rect = text_1.get_rect()
            text_1_1 = screen.get_width() / 2 - text_rect.width / 2
            text_1_2 = screen.get_width() / 2 - text_rect.height / 2
            screen.blit(text_1, [text_1_1, text_1_2])
        pygame.display.update()
GAME()