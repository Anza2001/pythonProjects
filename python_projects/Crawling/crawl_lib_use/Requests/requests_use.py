#  -*- UTF-8 -*- #
"""
@filename:requests_use.py
@author:Anza
@time:2023-07-25
"""
import time

import requests
import re


def req_baidu():
    r = requests.get('https://www.baidu.com')
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)


def req_get_use():
    r = requests.get('http://httpbin.org/get?name=anza&age=23')
    print(r.text)
    print(r.json())


def req_post_use():
    data = {'name': 'anza', 'age': '23'}
    r = requests.post('http://httpbin.org/post', data=data)
    print(r.text)


def req_file_upload():
    files = {'file': open('favicon.ico', 'rb')}
    r = requests.post('https://httpbin.org/post', files=files)
    print(r.text)


def get_zhihu_explore():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OX X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


def get_github_ico():
    r = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def sign_in_zhihu():
    headers = {
        'Cookie': '_zap=4a4a1470-f2e3-4495-ac6a-30d9bb709740; d_c0=AABX-blMohaPTgWvq0XqapDABvFRTcqvaeU=|1681628871; YD00517437729195%3AWM_TID=FKN35f7ub2BBEUEUVUaFatDyvbhOlNr8; _xsrf=27oy2MPSyHnMKvxFAbvJtui74m16yVV0; __snaker__id=7IBuO1Pfcc3IJad2; YD00517437729195%3AWM_NI=niDG8hOjSjJXc%2F%2F4sCH9JfVclNyozeLfLl1Lwhaglht9gZdMAYjcN8aCIhe11lvv7Qg%2BAi7wnajn3vCz4QKPtJmtNuh49elvU4ofY%2BnMQo34qEesYCOZMi%2BC%2BHBRnEYBbmg%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eedaf64fa3aca4b7ca21f1bc8ab2c84a939e8bacd574fb9db7bbe57cf5abfc89fb2af0fea7c3b92aaeb78ca8bb648db69d8bc954a1f1e1d5f2498ce78687d569b092b790f96f90ba848db448b5b8af88ef64b8e7a9bbe7478387a684cd34a39d8789e83bf3b4ba97b65ba5f58f8ab67daebfa68fb27e81a6fcb2ca5cb896a395cd7facecf786ef7e97eca187dc21ae939f90b240b39bab94dc498d86838aaa49e9988eb3ed4f9b9eae8ee637e2a3; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1690277148,1690292943,1690344040,1690348793; captcha_session_v2=2|1:0|10:1690348793|18:captcha_session_v2|88:b2gvSFlNUTdmOXAxUlpTc0VLUzZ5M09qdnQ1S1ZIOFFZY0llVXVKa3gxWTd1MWg3Yy96NGJ4bmNWanR4aEd4cQ==|3f998aa519add6e5fcaf46acce29ec5875e5f4c548da1d19304185736ca0fdf4; SESSIONID=CfG9MNdtmdju3DI7xlUv32WfSMow7thG4UZ1aAolmzy; JOID=UlAWAUhDWHM4EC-HV0HTJvKrYS5CCDU1AF5p6CItNBJMImjGa7n-s14bLI1XJjG2lizSRWzyDqgAkqbnMaskyQ0=; osd=UF4QAENBVnU5Gy2JUUDYJPytYCVABjM0C1xn7iMmNhxKI2PEZb__uFwVKoxcJD-wlyfQS2rzBaoOlKfsM6UiyAY=; gdxidpyhxdE=Vtj8B1g2sOhYRgUVCJsSsGzxZT4l%2B3UTn6uqmzcTj%5C29cGbc3vipk7m%5CtDq1yjgn9BiyW4IRPJoNhIcnQ2KHyQj35VKJ5omTezByNdLl1okCuzNdM81fji4TsyRgvKr3JQeSSoDGXPgfLkmpofATYDWGKUjfaZhYj27vtcWM3YneM6xB%3A1690349693578; o_act=login; ref_source=other_https://www.zhihu.com/signin?next=/; expire_in=15552000; q_c1=6f08f4fc3d8b4ae6a601e614f8549316|1690348802000|1690348802000; tst=r; z_c0=2|1:0|10:1690348804|4:z_c0|92:Mi4xb3MtbkNBQUFBQUFBQUZmNXVVeWlGaGNBQUFCZ0FsVk5BdnV0WlFBLVBKdV9FXzZVVDN4SS0yVGN6VU1sV3l3SFdR|d94417d05082994e174f789fad70c92f6bacb1b697df8c074f75319b0e9e8eea; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1690350184; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1690350184|1690348792',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OX X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)


def build_session():
    # 利用Session()创建一次会话
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


def test_non_CA():
    r = requests.get('https://www.12306.cn', verify=False)
    print(r.status_code)


def regex_html():
    html = '''  <li>
 <input type="checkbox" value="59930@" name="Url" class="check">
 <span class="songNum topRed">01.</span>
 <a target="_1" href="/play/59930.htm" class="songName cBlue">突然的自我 </a>
 </li>
   <li>
 <input type="checkbox" value="64541@" name="Url" class="check">
 <span class="songNum topRed">02.</span>
 <a target="_1" href="/play/64541.htm" class="songName ">天路 </a>
 </li>
   <li>
 <input type="checkbox" value="30001@" name="Url" class="check">
 <span class="songNum topRed">03.</span>
 <a target="_1" href="/play/30001.htm" class="songName cBlue">光辉岁月 </a>
 </li>
   <li>
 <input type="checkbox" value="1903@" name="Url" class="check">
 <span class="songNum ">04.</span>
 <a target="_1" href="/play/1903.htm" class="songName ">雨蝶 </a>
 </li>
   <li>
 <input type="checkbox" value="42620@" name="Url" class="check">
 <span class="songNum ">05.</span>
 <a target="_1" href="/play/42620.htm" class="songName ">千千阙歌 </a>
 </li>
   <li>
 <input type="checkbox" value="65937@" name="Url" class="check">
 <span class="songNum ">06.</span>
 <a target="_1" href="/play/65937.htm" class="songName ">再回首 </a>
 </li>
   <li>
 <input type="checkbox" value="11417@" name="Url" class="check">
 <span class="songNum ">07.</span>
 <a target="_1" href="/play/11417.htm" class="songName cBlue">大海 </a>
 </li>
   <li>
 <input type="checkbox" value="1462@" name="Url" class="check">
 <span class="songNum ">08.</span>
 <a target="_1" href="/play/1462.htm" class="songName ">甘心情愿 </a>
 </li>
   <li>
 <input type="checkbox" value="66417@" name="Url" class="check">
 <span class="songNum ">09.</span>
 <a target="_1" href="/play/66417.htm" class="songName ">爱拼才会赢 </a>
 </li>
   <li>
 <input type="checkbox" value="56770@" name="Url" class="check">
 <span class="songNum ">10.</span>
 <a target="_1" href="/play/56770.htm" class="songName ">单身情歌 </a>
 </li>
   <li>
 <input type="checkbox" value="81667@" name="Url" class="check">
 <span class="songNum ">11.</span>
 <a target="_1" href="/play/81667.htm" class="songName ">千年等一回 《新白娘子传奇》电视剧主题曲 </a>
 </li>
   <li>
 <input type="checkbox" value="1601@" name="Url" class="check">
 <span class="songNum ">12.</span>
 <a target="_1" href="/play/1601.htm" class="songName ">涛声依旧 </a>
 </li>
   <li>
 <input type="checkbox" value="89467@" name="Url" class="check">
 <span class="songNum ">13.</span>
 <a target="_1" href="/play/89467.htm" class="songName cBlue">日不落 </a>
 </li>
   <li>
 <input type="checkbox" value="35721@" name="Url" class="check">
 <span class="songNum ">14.</span>
 <a target="_1" href="/play/35721.htm" class="songName ">我只在乎你 </a>
 </li>
   <li>
 <input type="checkbox" value="82151@" name="Url" class="check">
 <span class="songNum ">15.</span>
 <a target="_1" href="/play/82151.htm" class="songName ">走过咖啡屋 </a>
 </li>
   <li>
 <input type="checkbox" value="179782@" name="Url" class="check">
 <span class="songNum ">16.</span>
 <a target="_1" href="/play/179782.htm" class="songName ">新贵妃醉酒 </a>
 </li>
   <li>
 <input type="checkbox" value="199353@" name="Url" class="check">
 <span class="songNum ">17.</span>
 <a target="_1" href="/play/199353.htm" class="songName ">你的柔情我永远不懂 </a>
 </li>
   <li>
 <input type="checkbox" value="24865@" name="Url" class="check">
 <span class="songNum ">18.</span>
 <a target="_1" href="/play/24865.htm" class="songName ">九百九十九朵玫瑰 </a>
 </li>
   <li>
 <input type="checkbox" value="187601@" name="Url" class="check">
 <span class="songNum ">19.</span>
 <a target="_1" href="/play/187601.htm" class="songName ">梦里水乡 </a>
 </li>
   <li>
 <input type="checkbox" value="408690@" name="Url" class="check">
 <span class="songNum ">20.</span>
 <a target="_1" href="/play/408690.htm" class="songName ">雨花石 </a>
 </li>
   <li>
 <input type="checkbox" value="91161@" name="Url" class="check">
 <span class="songNum ">21.</span>
 <a target="_1" href="/play/91161.htm" class="songName cRed">青花瓷 </a>
 </li>
   <li>
 <input type="checkbox" value="48517@" name="Url" class="check">
 <span class="songNum ">22.</span>
 <a target="_1" href="/play/48517.htm" class="songName ">上海滩 《上海滩》电视剧主题曲 </a>
 </li>'''
    pattern = '<a.*?>(.*?)\s</a>'
    result = re.search(pattern, html, re.S)
    print(result.group())
    results = re.findall(pattern, html, re.S)
    print(results)


def get_maoyan_top100(offset):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OX X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36',
    }

    url = 'https://www.maoyan.com/board/4?offset={}&requestCode=78d15a82e0d76a0722d535cf6fdc0b90ibp1y'.format(offset)
    r = requests.get(url, headers=headers)

    pattern = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)" alt="(.*?)".*?</a>.*?star.*?>(.*?)</p>' \
              '.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'

    if r.status_code == 200:
        # print(r.text)
        results = re.findall(pattern, r.text, re.S)
        for result in results:
            print('\nindex:', result[0])
            print('image:', result[1])
            print('title:', result[2])
            print('actor:', result[3].strip()[3:])
            print('time:', result[4][5:])
            print('score:', result[5].strip()+result[6].strip())
    else:
        print('Failed!')

if __name__ == '__main__':
    for offset in range(0, 100, 10):
        get_maoyan_top100(offset)
        time.sleep(1)
