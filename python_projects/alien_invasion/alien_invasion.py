#  -*- UTF-8 -*- #
"""
@filename:alien_invasion.py
@author:Anza
@time:2023-07-01
"""

import sys
import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien


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
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == '__main__':
    run_game()
