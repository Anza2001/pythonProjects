#  -*- UTF-8 -*- #
"""
@filename:weibo.py.py
@author:Anza
@time:2023-07-29
"""


from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq


base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(since_id=None):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'since_id': since_id,
    }
    url = base_url+urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json = response.json()
            items = json.get('data').get('cardlistInfo')
            return json, items['since_id']
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            print(weibo)


if __name__ == '__main__':
    since_id = None
    for i in range(5):
        json, since_id = get_page(since_id=since_id)
        parse_page(json)

