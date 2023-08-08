#  -*- UTF-8 -*- #
"""
@filename:user_agent.py
@author:Anza
@time:2023-08-04
"""


import requests
from parsel import Selector
url = "http://localhost:8205/verify/uas/index.html"


if __name__ == '__main__':
    """
    若默认User-Agent,返回码为403
    """
    header = {
        'User-Agent': 'Postman'
    }
    r = requests.get(url, headers=header)
    print(r.status_code)
    if r.status_code == 200:
        sel = Selector(r.text)
        res = sel.css(".list-group-item::text").extract()
        print(res)
    else:
        print('This request failed~')
