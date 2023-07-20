#  -*- UTF-8 -*- #
"""
@filename:hn_submissions.py
@author:Anza
@time:2023-07-20
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

if __name__ == '__main__':
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    print("Status code:", r.status_code)

    # 处理有关每篇文章的信息
    submission_ids = r.json()
    submission_dicts = []
    titles = []
    for submission_id in submission_ids[:10]:
        # 对于每篇文章都执行一个API调用
        url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
        submission_r = requests.get(url)
        print(submission_r.status_code)
        response_dict = submission_r.json()
        titles.append(response_dict['title'])
        submission_dict = {
            'value': response_dict.get('descendants', 0),
            'title': response_dict['title'],
            'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link", submission_dict['link'])
        print("Comments", submission_dict['value'])


    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-discussed news'
    chart.x_labels = titles
    chart.add('', submission_dicts)
    chart.render_to_file('news.svg')
