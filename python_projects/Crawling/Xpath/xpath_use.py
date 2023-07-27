#  -*- UTF-8 -*- #
"""
@filename:xpath_use.py
@author:Anza
@time:2023-07-26
"""

# etree可以用于修正HTML，补齐某些元素使其闭合
from lxml import etree


def generate_file():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
             <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
             <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
         </ul>
     </div>
    '''
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result)
    with open("test.html", 'wb') as f:
        f.write(result)


def find_child():
    html = etree.parse("./test.html", etree.HTMLParser())
    result = html.xpath('//li/a')
    print(result)


def find_parent():
    html = etree.parse("./test.html", etree.HTMLParser())
    result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
    print(result)


def get_attribute():
    html = etree.parse("./test.html", etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]')
    print(result)


def get_text():
    html = etree.parse("./test.html", etree.HTMLParser())
    result = html.xpath('//li[@class="item-0"]/a/text()')
    print(result)


if __name__ == '__main__':
    # find_child()
    # find_parent()
    # get_attribute()
    get_text()
