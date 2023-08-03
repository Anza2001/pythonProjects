#  -*- UTF-8 -*- #
"""
@filename:mitm_dedao.py
@author:Anza
@time:2023-08-02
"""


from mitmproxy import ctx
import json


def response(flow):
    url = "https://entree.igetget.com/ebook2/v1/ebook/list"
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title': book.get('book_name'),
                'cover': book.get('cover'),
                'author': book.get('book_author'),
                'intro': book.get('book_intro'),
            }
            print("=============================")
            print(data)



# if __name__ == '__main__':
#     print("Hello Python")
