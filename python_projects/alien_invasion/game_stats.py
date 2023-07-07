#  -*- UTF-8 -*- #
"""
@filename:game_stats.py
@author:Anza
@time:2023-07-05
"""

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 任何时候都不应该重置最高分
        self.high_score = 0
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

