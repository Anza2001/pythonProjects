#  -*- UTF-8 -*- #
"""
@filename:bs_use.py
@author:Anza
@time:2023-07-27
"""


from bs4 import BeautifulSoup


def basic_use():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    soup = BeautifulSoup(html, 'lxml')
    print("==========================================================")
    print(soup.prettify())
    # string用于获取文本
    print("==========================================================")
    print(soup.title.string)
    # name用于获取节点名称
    print("==========================================================")
    print(soup.title.name)
    # 获取head节点
    print("==========================================================")
    print(soup.head)
    # 获取第一个p节点
    print("==========================================================")
    print(soup.p)
    # 获取第一个p节点的属性,用attrs或者索引获取
    print("==========================================================")
    print(soup.p.attrs)
    print(soup.p.attrs['class'])
    print(soup.p['name'])
    # 获取第一个p节点的内容
    print("==========================================================")
    print(soup.p.string)
    # 获取body的所有直接子节点,用contents或者children
    print("==========================================================")
    print(soup.body.contents)
    print(soup.body.children)
    for i, child in enumerate(soup.body.children):
        print(i, child)
    # 获取body的所有子孙节点，用descendants
    print("==========================================================")
    print(soup.body.descendants)
    # 获取第一个a节点的父节点，用parent
    print("==========================================================")
    print(soup.a.parent)
    # 获取第一个a节点的祖父节点，用parents
    print("==========================================================")
    print(list(enumerate(soup.a.parents)))
    # 获取同级节点，用next_sibling(s)和previous_sibling(s)
    print("==========================================================")
    print(soup.a.next_sibling)
    print(soup.a.next_siblings)


def flex_use():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    # 寻找a标签
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find_all(name='a'))
    for a in soup.find_all(name='a'):
        print(a.string)
    # 寻找name属性为dromouse的标签
    print(soup.find_all(attrs={'name': 'dromouse'}))


def css_filter():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    # 寻找a标签
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('.sister'))
    print(soup.select('#link2'))
    print(soup.select('#link2')[0].get_text())


if __name__ == '__main__':
    # basic_use()
    # flex_use()
    css_filter()

