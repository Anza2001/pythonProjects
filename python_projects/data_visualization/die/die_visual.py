#  -*- UTF-8 -*- #
"""
@filename:die_visual.py
@author:Anza
@time:2023-07-19
"""

from die import Die
import pygal

if __name__ == '__main__':
    # 创建一个Die类
    die = Die()

    # 投掷几次骰子，并将结果存储在一个列表中
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    hist = pygal.Bar()
    hist.title = "Results of rolling one D6 1000 times"
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')

