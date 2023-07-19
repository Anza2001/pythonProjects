#  -*- UTF-8 -*- #
"""
@filename:die.py
@author:Anza
@time:2023-07-19
"""

from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)


