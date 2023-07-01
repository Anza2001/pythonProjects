#  -*- UTF-8 -*- #
"""
@filename:ship.py
@author:Anza
@time:2023-07-01
"""

import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船设置"""
        self.screen = screen
        self.ship_width = 55
        self.ship_height = 65

        # 记载飞船图像并获取外接矩阵
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.png'),
            (self.ship_width, self.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
