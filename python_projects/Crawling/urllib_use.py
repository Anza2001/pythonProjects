#  -*- UTF-8 -*- #
"""
@filename:tools.py
@author:Anza
@time:2023-07-23
"""

from urllib import request, parse, error
import http.cookiejar, urllib.request
from urllib.robotparser import RobotFileParser

def urllib_tool():
    # response = urllib.request.urlopen('https://www.python.org/')
    # print(response.read().decode('utf-8'))
    # print(type(response))
    # print(response.status)
    # print(response.getheaders())
    # print(response.getheader('Server'))

    # data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    # response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=1)
    # print(response.read())

    url = 'http://httpbin.org/post'

    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org',
    }
    dict = {
        'name': 'Germey',
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))

def get_cookies():
    filename = 'cookies.txt'
    url = 'http://www.baidu.com'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    # cookie.load('cookies.txt', ignore_expires=True, ignore_discard=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    for item in cookie:
        print(item.name+" = "+item.value)

def error_handle():
    try:
        rep = request.urlopen("https://anza2001.github.io/nono.html")
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print("Request Successfully")

def test_robots():
    rp = RobotFileParser()
    rp.set_url('http://www.jianshu.com/robots.txt')
    rp.read()
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

if __name__ == '__main__':
    # urllib_tool()
    # get_cookies()
    # error_handle()
    test_robots()
