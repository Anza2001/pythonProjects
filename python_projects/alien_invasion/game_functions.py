#  -*- UTF-8 -*- #
"""
@filename:game_functions.py
@author:Anza
@time:2023-07-01
"""

import sys
import pygame

def check_events():
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    """更新屏幕图像"""

