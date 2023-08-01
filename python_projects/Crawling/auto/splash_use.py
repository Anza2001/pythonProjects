#  -*- UTF-8 -*- #
"""
@filename:splash_use.py
@author:Anza
@time:2023-07-31
"""


import requests
from urllib.parse import quote
base_url = 'http://localhost:8050/'


def render_html():
    # url = base_url+"render.html?url=https://www.baidu.com"
    url = base_url + "render.html?url=https://www.taobao.com&wait=5"
    r = requests.get(url)
    print(r.text)


def render_png():
    url = base_url+"render.png?url=https://www.jd.com&wait=5&width=1000&height=700"
    r = requests.get(url)
    with open("jd.png", 'wb') as f:
        f.write(r.content)


def render_har():
    url = base_url+"render.har?url=https://www.jd.com&wait=5"
    r = requests.get(url)
    print(r.json())


def render_json():
    # html=1则会传入源代码，har=1则会传入页面HAR数据
    url = base_url+"render.json?url=https://httpbin.org&html=1&har=1"
    r = requests.get(url)
    print(r.text)


def exe():
    lua = '''
    function main(splash, args)
        local treat = require("treat")
        local response = splash:http_get("http://httpbin.org/get")
            return {
                html=treat.as_string(response.body),
                url=response.url,
                status=response.status
            }
    end
    '''
    url = base_url+"execute?lua_source="+quote(lua)
    r = requests.get(url)
    print(r.text)


if __name__ == '__main__':
    # render_html()
    # render_png()
    # render_har()
    # render_json()
    exe()
