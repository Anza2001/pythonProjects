#  -*- UTF-8 -*- #
"""
@filename:selenium.py
@author:Anza
@time:2023-07-29
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

path = Service('chromedriver.exe')


def init_browser():
    option = webdriver.ChromeOptions()
    # 防止自动退出
    option.add_experimental_option("detach", True)
    browser = webdriver.Chrome(service=path, options=option)
    return browser


def basic_use(browser):
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element(By.ID, "kw")
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        # print(browser.get_cookies())
        # print(browser.page_source)
    # finally:
    #     browser.close()
    except:
        print("failed")


def visit_taobao(br):
    br.get('https://www.taobao.com')
    # input1 = br.find_element(By.ID, "q")
    # input2 = br.find_element(By.NAME, "q")
    # input3 = br.find_element(By.XPATH, '//*[@id="q"]')
    # print(input1, input2, input3)
    item = br.find_element(By.ID, 'q')
    item.send_keys('iPhone')
    time.sleep(1)
    item.clear()
    item.send_keys('iPad')


def action_chain(br):
    url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    br.get(url)
    br.switch_to.frame('iframeResult')
    source = br.find_element(By.ID, "draggable")
    target = br.find_element(By.ID, "droppable")
    actions = ActionChains(br)
    actions.drag_and_drop(source, target)
    actions.perform()


def js_imitate(br):
    url = "https://www.zhihu.com/explore"
    br.get(url)
    br.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    br.execute_script('alert("To Bottom")')


def get_node_info(br):
    url = "https://www.zhihu.com/explore"
    br.get(url)
    ele = br.find_element(By.ID, "guestSquare")
    print(ele)
    print(ele.get_attribute('class'))


if __name__ == '__main__':
    browser = init_browser()
    # basic_use(browser)
    # browser.get('http://www.baidu.com')
    # print(browser.title)
    # visit_taobao(browser)
    # action_chain(browser)
    # js_imitate(browser)
    get_node_info(browser)

