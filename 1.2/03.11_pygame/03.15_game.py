import pygame
import random

WIDTH = 1920
HEIGHT = 820
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Победи зло!")
clock = pygame.time.Clock()

bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg, (1920, 820))
rect = bg.get_rect()
rect = rect.move((0, 0))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.x = self.rect.centerx = WIDTH / 5
        self.y = self.rect.bottom = HEIGHT - 10

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Monster1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('monster4.gif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 340))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1000 - self.rect.width, 1500 - self.rect.width)
        self.rect.y = random.randrange(HEIGHT // 2 - 100, HEIGHT // 2 - 75)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x -= 3

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y + y // 2 - 50
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
monsters = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(4):
    m1 = Monster1()
    all_sprites.add(m1)
    monsters.add(m1)

swag = True
while swag:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            swag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                swag = False

    all_sprites.update()

    hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
    for hit in hits:
        m1 = Monster1()
        all_sprites.add(m1)
        monsters.add(m1)

    hits = pygame.sprite.spritecollide(player, monsters, False)
    if hits:
        from test import*
        swag = False
    screen.blit(bg, rect)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
