#  -*- UTF-8 -*- #
"""
@filename:different_dice.py
@author:Anza
@time:2023-07-19
"""

import pygal
from die import Die

if __name__ == '__main__':
    die_1 = Die()
    die_2 = Die(10)

    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 可视化结果
    hist = pygal.Bar()
    hist.title = "Result of rolling D6+D10 dices 50000 times"
    hist.x_labels = [str(i) for i in range(2, max_result+1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6+D10', frequencies)
    hist.render_to_file('different_dice.svg')
