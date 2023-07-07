#  -*- UTF-8 -*- #
"""
@filename:settings.py
@author:Anza
@time:2023-07-01
"""

class Settings():
    """存储设置参数"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 0.5
        self.alien_drop_speed = 25
        self.alien_points = 50

        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """随游戏动态变化的设置"""
        self.ship_speed = 1
        self.bullet_speed = 1
        self.alien_speed = 0.5

        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
