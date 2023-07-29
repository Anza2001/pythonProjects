#  -*- UTF-8 -*- #
"""
@filename:storage.py
@author:Anza
@time:2023-07-27
"""
import re
import requests
import json
import csv


def txt_storage():
    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OX X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36',
    }
    r = requests.get(url)
    html = r.text
    pattern = '<a.*?class="css-1nd7dqm".*?href="(.*?)">(.*?)</a>.*?<div.*?' \
              'class="css-13jrecd">(.*?)浏览 · (.*?)关注 · (.*?) 回答</div>'
    results = re.findall(pattern, html, re.S)
    print(results)
    with open('data.txt', 'wb') as f:
        for i in range(len(results)):
            if i == 0:
                f.write("=========近期热点=========\n".encode('utf-8'))
            elif i == 4:
                f.write("\n=========潜力好问题=========\n".encode('utf-8'))

            k = i+1 if i < 4 else i-3
            content = str(k)+"——"+results[i][1]+"\n"
            content += "url: "+results[i][0]+"\n"
            content += results[i][2]+"浏览-"+results[i][3]+"关注-"+results[i][4]+" 回答\n"
            f.write(content.encode('utf-8'))


def json_storage():
    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OX X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36',
    }
    r = requests.get(url)
    html = r.text
    pattern = '<a.*?class="css-1nd7dqm".*?href="(.*?)">(.*?)</a>.*?<div.*?' \
              'class="css-13jrecd">(.*?)浏览 · (.*?)关注 · (.*?) 回答</div>'
    results = re.findall(pattern, html, re.S)
    print(results)
    content = []
    for i in range(len(results)):
        c = {
            "about": "近期热点" if i < 4 else "潜力好问题",
            "title": results[i][1],
            "url": results[i][0],
            "view": results[i][2]+"浏览",
            "interest": results[i][3]+"关注",
            "answer": results[i][4]+" 回答",
        }
        content.append(c)
    with open("data.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(content, indent=2, ensure_ascii=False))


def csv_storage():
    with open("data.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['10001', 'Mike', 20])
        writer.writerow(['10002', 'Bob', 22])
        writer.writerow(['10003', 'Jordan', 21])

    with open('data.csv', 'a') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'id': '10004',
                         'name': 'anza',
                         'age': 23})


if __name__ == '__main__':
    # txt_storage()
    # json_storage()
    # with open('data.json', 'r', encoding='utf-8') as f:
    #     s = f.read()
    #     data = json.loads(s)
    #     print(data)
    csv_storage()

