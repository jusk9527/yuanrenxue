import requests
import time
import execjs
import re

session = requests.Session()



# headers = {
#     'authority': 'match.yuanrenxue.com',
#     'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'dnt': '1',
#     'x-requested-with': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     "User-Agent": "yuanrenxue.project",
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://match.yuanrenxue.com/match/13',
#     'accept-language': 'zh-CN,zh;q=0.9',
# }

headers = {"User-Agent": "yuanrenxue.project", }


def get_result():
    url = "http://match.yuanrenxue.com/match/13"

    r = session.get(url)

    print(r.text)

    # 每次都是一个全新的js 所以每次得重新请求得到，下面那个固定了。没用，时间戳会变

    # sum = 0
    # ctx = execjs.compile(open(file).read())
    # res = ctx.call('get_cookie')
    #
    # cookie = res.replace(';path=/','')


    # print(cookie)

    reg = re.compile("'([a-zA-Z0-9=|_])'")

    results = reg.findall(r.text)

    cookie = ''.join(results)

    print(cookie)

    key, value = cookie.split('=')

    session.cookies.set(key, value)

    sum = 0

    for i in range(1, 6):
        response = session.get(f'https://match.yuanrenxue.com/api/match/13?page={i}',headers=headers)

        print(response.text)

        for j in response.json().get('data'):
            sum += j["value"]

        time.sleep(1)
    return sum


res = get_result()
print("结果为: "+str(res))
# 结果为: 213133
