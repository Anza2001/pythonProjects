#  -*- UTF-8 -*- #
"""
@filename:toutiao.py
@author:Anza
@time:2023-07-29
"""

from urllib.parse import urlencode
import requests
import os


base_url = 'https://so.toutiao.com/search?'
# 需要加Cookie,否则会报错
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    'Host': 'so.toutiao.com',
    'Cookie': 'msToken=N27h6UrB-xNyXrTGBbnhzd0FSZLFgCMQtqXD2kvdHk1FP5BhUUHoCLuee50mJf6Wr_SYVh5NST1asr21Qql7VL9pQn0XiYDV-znJyJ5S; tt_webid=7261141969258694202; _ga_QEHZPBE5HH=GS1.1.1690616366.1.0.1690616366.0.0.0; _ga=GA1.1.1765861084.1690616366; ttwid=1%7C_cgn6gFdBorS9MuubcpJ0ide4ZfRFIoojF3CpXHI9p4%7C1690616366%7C8cfb586be2443fd5c9fb7b15cfc86889f2204b46fca6dafab71ca8226260cd75; _tea_utm_cache_4916=undefined; _S_DPR=2; _S_IPAD=0; s_v_web_id=verify_lknpcji3_Wqa23XQj_dkiN_4gTw_BYmL_4ozHfxUrOGvU; _S_WIN_WH=1440_273'
}


def get_page(page_num=1):
    params = {
        'keyword': '猫猫',
        'pd': 'atlas',
        'dvpf': 'pc',
        'aid': 4916,
        'page_num': page_num,
        'search_json': {"from_search_id":"2023072915530873DA629D22B59A8C14F8","origin_keyword":"街拍","image_keyword":"街拍"},
        'source': 'input',
        'rawJSON': 1,
        'search_id': '20230729155700018116674CC7A080A180'
    }
    url = base_url + urlencode(params)
    # print(url)

    r = requests.get(url, headers=headers)
    json = r.json()
    return json

    # try:
    #     r = requests.get(url, headers=headers)
    #     print(r.json())
    # except:
    #     print('failed!')


def parse_page(json):
    if json:
        items = json.get('rawData').get('data')
        for item in items:
            info = {}
            info['img_url'] = item['img_url']
            info['text'] = item['text']
            print(info)


if __name__ == '__main__':
    page = get_page()
    parse_page(page)
