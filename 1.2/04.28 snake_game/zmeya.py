import pygame
import random
import pygame_menu
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
bg_menu = pygame.image.load('menu_back.jpg')
black = (0, 0, 0)
white = (255, 255, 255)
snake = (0, 0, 0)
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('АДСКАЯ ЗМЕЙКА')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("monospace", 99)
font_style2 = pygame.font.SysFont("monospace", 30)
score_font = pygame.font.SysFont("Verdana", 20)
bg = pygame.image.load('back.jpg')
bg = pygame.transform.scale(bg, (750, 700))
rect = bg.get_rect()

def score(score):
    value = score_font.render("SCORE: " + str(score), True, black)
    screen.blit(value, [300, 0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, snake, [x[0], x[1], snake_block, snake_block])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 25, height / 3])
def message2(msg, color):
    mesg = font_style2.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 2])
def gameLoop():
    pygame.mixer.music.load("fight.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=30)
    pygame.mixer.music.set_volume(0.4)
    game_over = False
    game_close = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(100, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(100, height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
            pygame.mixer.music.set_volume(1)
            message("GAME OVER!!!", white)
            message2("ESC - EXIT; SPACE - CONTINUE", white)
            score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        apple = (0, 255, 0)
        pygame.draw.rect(screen, apple, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(100, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(100, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            # s_catch = pygame.mixer.music.load('apple.ogg')
            # s_catch = pygame.mixer.music.play(1)
            # s_catch.play(1)
        clock.tick(snake_speed)
        screen.blit(bg, rect)
        pygame.display.update()
    pygame.quit()
    quit()


main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.0)
main_theme.title_background_color=(0, 0, 0, 0)
font = pygame_menu.font.FONT_8BIT
main_theme.widget_font=font
menu = pygame_menu.Menu('', 350, 200, theme=main_theme)
menu.add.button('PLAY', gameLoop)
menu.add.button('EXIT', pygame_menu.events.EXIT)
pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=30)
pygame.mixer.music.set_volume(0.7)
while True:
    screen.blit(bg_menu, (0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)
    pygame.display.update()
gameLoop()
