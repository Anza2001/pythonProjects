#  -*- UTF-8 -*- #
"""
@filename:rw_visual.py
@author:Anza
@time:2023-07-19
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    while True:
        rw = RandomWalk()
        rw.fill_walk()

        # 设置绘画窗口的尺寸
        plt.figure(dpi=128, figsize=(10, 6))

        point_numbers = list(range(rw.num_points))

        # 隐藏坐标，《Python编程——从入门到实践》书上例子已不适用
        # 参考博客：https://blog.csdn.net/Azad221103/article/details/124956008
        # plt.axes().get_xaxis().set_visible(False)
        # plt.axes().get_yaxis().set_visible(False)
        current_axes = plt.axes()
        current_axes.xaxis.set_visible(False)
        current_axes.yaxis.set_visible(False)

        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                    edgecolors='none', s=15)
        # 突出起点与终点
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        plt.show()

        keep_running = input("Make another walk? (y/n):")
        if keep_running == 'n':
            break