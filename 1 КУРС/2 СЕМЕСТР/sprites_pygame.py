import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1920, 820), pygame.RESIZABLE)
pygame.display.set_caption("ПОБЕДИ ЗЛО!")

clock = pygame.time.Clock()

x = 50
y = 380
x_monster1 = 1300
y_monster1 = 450

x_monster2 = 900
y_monster2 = 450

x_monster3 = 1300
y_monster3 = 200

x_monster4 = 1000
y_monster4 = 200

width = 175
height = 250
speed = 5
isJump = False
Jump = 10
enemySpeed = 1

bg = pygame.image.load('background.jpg')

player_image = pygame.image.load('player.png')

monster1_image = pygame.image.load('monster1.gif')
monster1_image = pygame.transform.scale(monster1_image, (350, 350))

monster2_image = pygame.image.load('monster2.gif')
monster2_image = pygame.transform.scale(monster2_image, (600, 350))

monster3_image = pygame.image.load('monster3.png')
monster3_image = pygame.transform.scale(monster3_image, (300, 300))

monster4_image = pygame.image.load('monster4.gif')
monster4_image = pygame.transform.scale(monster4_image, (300, 300))

bg = pygame.transform.scale(bg, (1920, 820))
rect = bg.get_rect()
rect = rect.move((0, 0))

player = pygame.sprite.Sprite()
monster1 = pygame.sprite.Sprite()
monster2 = pygame.sprite.Sprite()
monster3 = pygame.sprite.Sprite()
monster4 = pygame.sprite.Sprite()

def draw():
    screen.blit(bg, rect)

def playerInit():
    global player
    screen.blit(player_image, (x, y))

def monster1Init():
    global monster1
    screen.blit(monster1_image, (x_monster1, y_monster1))

def monster2Init():
    global monster2
    screen.blit(monster2_image, (x_monster2, y_monster2))

def monster3Init():
    global monster3
    screen.blit(monster3_image, (x_monster3, y_monster3))

def monster4Init():
    global monster4
    screen.blit(monster4_image, (x_monster4, y_monster4))
    pygame.display.update()

monsters = pygame.sprite.Group()
monsters.add(monster1, monster2, monster3, monster4)

player_group = pygame.sprite.Group()
player_group.add(player)

swag = True
while swag:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            swag = False
    x_monster1 -= 2 and x > 1
    x_monster2 -= 2 and x > 1
    x_monster3 -= 2 and x > 1
    x_monster4 -= 2 and x > 1

    # Команды движения
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 5:
        x -= speed
    if keys[pygame.K_d] and x < 950:
        x += speed
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if Jump >= -10:
            if Jump < 0:
                y += (Jump ** 2) / 2
            else:
                y -= (Jump ** 2) / 2
            Jump -= 1
        else:
            isJump = False
            Jump = 10

    # hits = pygame.sprite.spritecollide(player, monsters, False)
    # if hits:
    #     swag = False

    draw()
    playerInit()
    monster1Init()
    monster2Init()
    monster3Init()
    monster4Init()
    monsters.update()
    pygame.display.update()

pygame.quit()