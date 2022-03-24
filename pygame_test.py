import pygame
import sys
import math
import random
#from pygame.sprite import Sprite
#from pygame.sprite import Group

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960
SHIP_SPEED_FACTOR = 6
BULLET_SPEED_FACTOR = 10
ENEMY_SPEED_FACTOR = 5
NUM_OF_ENEMIES = 10
SCORE = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg_color=(80,80,80)
pygame.display.set_caption("ROCKET")
background_image = pygame.image.load("alien_invasion/images/bgimg.png")

font = pygame.font.SysFont('SimHei', 72)
font2 = pygame.font.SysFont('Arial', 36)
game_win = font.render('获得胜利！', 1, (255, 255, 255))

def show_score():
    txt_score = f"SCORE: {SCORE}"
    t_score = font2.render(txt_score, 1, (255, 0, 0))
    screen.blit(t_score, (15, 15))

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('alien_invasion/images/rocket2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def keepmoving(self):
        if self.moving_up and rocket.rect.top > 0:
            self.rect.centery -= SHIP_SPEED_FACTOR
        if self.moving_down and rocket.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += SHIP_SPEED_FACTOR
        if self.moving_left and rocket.rect.left > 0:
            self.rect.centerx -= SHIP_SPEED_FACTOR
        if self.moving_right and rocket.rect.right < self.screen_rect.right:
            self.rect.centerx += SHIP_SPEED_FACTOR

    def blitme(self):
        self.screen.blit(self.image, self.rect)

rocket = Rocket(screen)

class Enemy():
    def __init__(self):
        self.image = pygame.image.load("alien_invasion/images/enemy.png")
        self.x = random.randint(200, 800)
        self.y = random.randint(50, 200)
        self.speed = random.randint(1, 6)

enemies = []
for i in range(NUM_OF_ENEMIES):
    enemies.append(Enemy())

bullets = []

class Bullet():
    def __init__(self, rocket):
        self.image = pygame.image.load("alien_invasion/images/bullet.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = rocket.rect.centerx
        self.rect.bottom = rocket.rect.top
        self.speed = BULLET_SPEED_FACTOR

    def hit(self):
        global SCORE
        for enemy in enemies:
            if distance(self.rect.centerx, self.rect.centery, enemy.x + 64, enemy.y + 32) < 60:
                bullets.remove(self)
                enemies.remove(enemy)
                SCORE += 10

def show_bullet():
    for bullet in bullets:
        screen.blit(bullet.image, (bullet.rect.centerx, bullet.rect.centery))
        bullet.hit()
        bullet.rect.centery -= bullet.speed
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def show_enemies():
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.x, enemy.y))
        
        if enemy.x < 0 or enemy.x + 128 > SCREEN_WIDTH:
            enemy.speed *= -1
        
        enemy.x -= enemy.speed

def distance(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    return math.sqrt(a*a + b*b)

while True: #主循环
    screen.blit(background_image,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.moving_up = True
            if event.key == pygame.K_DOWN:
                rocket.moving_down = True
            if event.key == pygame.K_LEFT:
                rocket.moving_left = True
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            if event.key == pygame.K_SPACE:
                bullet = Bullet(rocket)
                bullets.append(bullet)
                #print("Current total amount of bullet in screen is "+ str(len(bullets)))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.moving_up = False
            if event.key == pygame.K_DOWN:
                rocket.moving_down = False
            if event.key == pygame.K_LEFT:
                rocket.moving_left = False
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False

    rocket.blitme()
    rocket.keepmoving()
    show_bullet()
    show_enemies()
    show_score()
    if len(enemies) < 1:
        screen.blit(game_win, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        
    pygame.display.update()
