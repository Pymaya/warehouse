import pygame
import sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg_color=(80,80,80)
pygame.display.set_caption("ROCKET")

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
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
            self.rect.centery -= 1
        if self.moving_down and rocket.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_left and rocket.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_right and rocket.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

rocket = Rocket(screen)

while True:
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.moving_up = False
            if event.key == pygame.K_DOWN:
                rocket.moving_down = False
            if event.key == pygame.K_LEFT:
                rocket.moving_left = False
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False

    screen.fill(bg_color)
    rocket.keepmoving()
    rocket.blitme()
    pygame.display.flip()
