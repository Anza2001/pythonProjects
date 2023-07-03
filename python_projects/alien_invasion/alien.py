#  -*- UTF-8 -*- #
"""
@filename:alien.py
@author:Anza
@time:2023-07-02
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """初始化外星人并设置其起始位置"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.alien_width = 60
        self.alien_height = 60

        # 加载外星人图像，并设置其 rect 属性
        self.image = pygame.transform.scale(
            pygame.image.load('images/alien.png'),
            (self.alien_width, self.alien_height))

        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
