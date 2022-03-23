import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gfunc

def run_game():
    #初始化游戏并创建游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)

    while True: #游戏主循环
        gfunc.check_events(ship)
        gfunc.update_screen(ai_settings,screen,ship)
        ship.update()
        
run_game()