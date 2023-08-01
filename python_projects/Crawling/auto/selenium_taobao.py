#  -*- UTF-8 -*- #
"""
@filename:selenium_taobao.py
@author:Anza
@time:2023-07-31
"""
import json
import time
import pymongo

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import urlencode
from pyquery import PyQuery as pq

path = Service('chromedriver.exe')
base_url = "https://s.taobao.com/search?"
has_cookie = 1

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def init_browser():
    option = webdriver.ChromeOptions()
    # 防止自动退出
    option.add_experimental_option("detach", True)
    browser = webdriver.Chrome(service=path, options=option)
    return browser


def get_cookies(log_url, browser):
    # 获取cookie保存在本地
    browser.get(log_url)
    time.sleep(20)
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)

    with open('taobao_cookies.txt', 'w') as f:
        f.write(jsonCookies)

    print("Cookies保存成功！")


def load_cookies(log_url, browser):
    browser.get(log_url)

    with open('taobao_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    for cookie in listCookies:
        cookie_dict = {
            'domain': '.taobao.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'path': '/',
            "expires": '',
            'sameSite': 'None',
            'secure': cookie.get('secure')
        }
        browser.add_cookie(cookie_dict)
    time.sleep(1)
    browser.get(log_url)


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert_one(result):
            print("存储到Mongo成功！")
    except Exception:
        print("存储到Mongo失败~")


def get_info(browser):
    # browser.execute_script("window.scrollTo(9, document.body.scrollHeight)")
    # time.sleep(3)
    html = browser.page_source
    doc = pq(html)
    items = doc('.Card--doubleCardWrapper--L2XFE73').items()
    for item in items:
        product = {
            'title': item.find(".Title--title--jCOPvpf").text(),
            'price': item.find(".Price--priceInt--ZlsSi_M").text()+
              item.find(".Price--priceFloat--h2RR0RK").text(),
            'shop': item.find(".ShopInfo--shopName--rg6mGmy").text(),
            'location': item.find(".Price--procity--_7Vt3mX").text(),
            'sales': item.find(".Price--realSales--FhTZc7U").text(),
            'url': item.attr("href"),
        }
        print(product)
        save_to_mongo(product)


if __name__ == '__main__':
    params = {
        'page': 1,
        'q': '小米手机'
    }
    url = base_url+urlencode(params)
    br = init_browser()
    if has_cookie == 1:
        load_cookies(url, br)
    else:
        get_cookies(url, br)
    get_info(br)
