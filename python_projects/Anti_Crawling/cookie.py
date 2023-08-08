#  -*- UTF-8 -*- #
"""
@filename:cookie.py
@author:Anza
@time:2023-08-04
"""

import requests
from lxml import etree
url = 'http://localhost:8207/verify/cookie/content.html'


if __name__ == '__main__':
    """
    如果没有cookie，将会被重定位至错误网址
    """
    header = {
        'Cookie': 'isfirst=789kq7uc1pp4c'
    }
    r = requests.get(url, headers=header)
    print(r.status_code)
    if r.status_code == 200:
        # print(r.text)
        html = etree.HTML(r.text)
        res = html.cssselect('.page-header h1')[0].text
        print(res)
    else:
        print("the request failed~")
