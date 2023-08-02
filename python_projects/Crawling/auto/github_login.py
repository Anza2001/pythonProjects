#  -*- UTF-8 -*- #
"""
@filename:github_login.py
@author:Anza
@time:2023-08-02
"""


from lxml import etree
import requests
import re


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Host': 'github.com',
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        r = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(r.text)
        token = selector.xpath('/html/body/div[1]/div[3]/main/div/div[4]/form/input[1]/@value')
        return token

    def login(self, email, pwd):
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': self.token(),
            'login': email,
            'password': pwd
        }
        r = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if r.status_code == 200:
            r = self.session.get("https://github.com/dashboard/my_top_repositories?location=left")
            self.print_repo(r.text)

    def print_repo(self, html):
        pattern = '<img src.*?class.*?width.*?height.*?alt="(.*?)".*?>'
        names = re.findall(pattern, html, re.S)
        for name in names:
            print(name)


if __name__ == '__main__':
    login = Login()
    login.login('email', 'pwd')
