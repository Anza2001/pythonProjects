#  -*- UTF-8 -*- #
"""
@filename:pyquery_use.py
@author:Anza
@time:2023-07-27
"""


from pyquery import PyQuery as pq


def basic_use():
    html = '''
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
    '''
    doc = pq(html)
    print(doc('li'))
    # 采用CSS选择器
    print(doc('#container .list li'))
    # 查找节点
    items = doc('.list')
    print(items)
    lis1 = items.find('li')
    print(lis1)
    lis2 = items.children('.active')
    print(lis2)
    lis3 = items.parent()
    print(lis3)
    li = doc(".list .item-0.active")
    print((li.siblings()))
    print("==============================================================")
    ll = doc('li').items()
    print(type(ll))
    for i, item in enumerate(ll):
        print(i, item)
        print(item.attr('class'))


def url_use():
    url = 'https://anza2001.github.io/'
    doc = pq(url=url)
    print(doc('title'))


if __name__ == '__main__':
    basic_use()
    # url_use()
