#  -*- UTF-8 -*- #
"""
@filename:sign.py
@author:Anza
@time:2023-08-05
"""


import requests
import hashlib
from time import time
from random import randint, sample
from lxml import etree
url = "http://localhost:8206/"


def hex_md5(value):
    # 使用md5加密值并返回加密后的字符串
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()


def generate_sign():
    """
    fet?actions=66827&tim=1691204927&randstr=LVOQU&sign=ac87f59be2e4c07521bd5981d443b0cd
    """
    # 生成5个1~9的随机数字，并进行拼接
    actions = "".join([str(randint(1, 9)) for _ in range(5)])
    # 生成当前时间戳
    tim = round(time())
    # 生成5个随机大写字母
    randstr = "".join(sample([chr(_) for _ in range(65, 91)], 5))
    # 3个参数拼接后进行MD5加密
    value = actions+str(tim)+randstr
    hexs = hex_md5(value)
    print(actions, tim, randstr, hexs)
    return actions, tim, randstr, hexs


if __name__ == '__main__':
    header = {
        'User-Agent': 'Postman'
    }
    actions, tim, randstr, hexs = generate_sign()
    uri = "fet?actions={}&tim={}&randstr={}&sign={}".format(actions, tim, randstr, hexs)
    target = url+uri
    r = requests.get(target)
    print(r.text)


