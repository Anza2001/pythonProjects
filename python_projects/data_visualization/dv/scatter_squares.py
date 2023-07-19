#  -*- UTF-8 -*- #
"""
@filename:scatter_squares.py
@author:Anza
@time:2023-07-19
"""

import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_values = list(range(1, 100))
    y_values = [x**2 for x in x_values]
    # plt.scatter(x_values, y_values, c='red', edgecolors='none', s=10)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)

    # 设置图表标并给坐标轴加上标签
    plt.title("Square Number", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # 设置刻度标记的大小
    plt.tick_params(axis="both", which='major', labelsize=14)

    # 设置每个坐标轴的取值范围
    plt.axis([0, 110, 0, 11000])

    # 第二个参数裁剪空余白边
    plt.savefig('squares_plt.png', bbox_inches='tight')
    plt.show()