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
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 0.5
        self.alien_drop_speed = 25
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
