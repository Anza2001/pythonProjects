#  -*- UTF-8 -*- #
"""
@filename:alien_invasion.py
@author:Anza
@time:2023-07-01
"""

import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    # 初始化背景
    pygame.init()
    ai_settings = Settings()
    # 创建显示窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

if __name__ == '__main__':
    run_game()
