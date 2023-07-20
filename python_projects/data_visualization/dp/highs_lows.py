#  -*- UTF-8 -*- #
"""
@filename:highs_lows.py
@author:Anza
@time:2023-07-19
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime

if __name__ == '__main__':
    filename = 'death_valley_2014.csv'

    # 获取最高气温数据
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # 打印文件头及位置
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    fig = plt.figure(dpi=80, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图片格式
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    # 绘制斜的日期
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
