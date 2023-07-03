#  -*- UTF-8 -*- #
"""
@filename:ship.py
@author:Anza
@time:2023-07-01
"""

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船设置"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.ship_width = 70
        self.ship_height = 70
        # 记载飞船图像并获取外接矩阵
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.png'),
            (self.ship_width, self.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # 移动标记
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed

        # self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
