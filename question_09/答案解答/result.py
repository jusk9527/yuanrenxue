import requests
import re
import os
import execjs

file = "./09_m.js"


def get_result(timestrip):
    sum = 0
    ctx = execjs.compile(open(file, encoding="utf-8").read())
    res = ctx.call('get_m', int(timestrip))

    return res


def main():
    client = requests.session()
    headers = {
        'User-Agent': 'yuanrenxue.project',
    }
    client.headers.update(headers)
    url = "http://match.yuanrenxue.com/match/9"
    response = client.get(url)
    # 匹配他返回的固定值
    re_timstrip = re.search(r"decrypt,'(\d+)'", response.text, re.S)
    ts = re_timstrip.group(1)
    nodejs = os.popen('node 09_m ' + ts)
    m = nodejs.read().replace('\n', '')
    nodejs.close()

    # 编码问题会导致结果错误
    # m_cookie = get_result(ts)

    cookie = requests.cookies.RequestsCookieJar()
    cookie.set('m', m)
    client.cookies.update(cookie)
    result_list = []

    for page in range(1, 6):
        res = client.get(
            'http://match.yuanrenxue.com/api/match/9?page={}'.format(str(page)), headers=headers)
        print(res.text)
        result_list += res.json()['data']

    # 总数
    total = 0
    # 个数
    count = 0
    for each in result_list:
        count += 1
        total += each['value']
    print('总数', total)
    print('平均', total / count)


if __name__ == '__main__':
    main()
    # 总数 245000
    # 平均 4900.0
