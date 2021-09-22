import requests
import execjs
import time

headers = {
    'authority': 'match.yuanrenxue.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'yuanrenxue.project',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.com/match/1',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1628664095; no-alert3=true; Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1628664332; m=bff0873b5164fa7c64b08d88344343b7|1628669372000; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1628670722; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1628677301; Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1628763084; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1628821487',
}

file = "/Users/xiao/PycharmProjects/yuanrenxue/question_01/答案解答/m结果.js"


def get_result():
    sum = 0
    num = 0

    ctx = execjs.compile(open(file).read())
    res = ctx.call('get_windos_f')

    for i in range(1, 6):
        params = (
            ('m', '{0}\u4E28{1}'.format(res['res1'], res['res2'])),
            ('page', i)

        )
        response = requests.get('https://match.yuanrenxue.com/api/match/1', headers=headers,params=params).json()

        for j in response.get('data'):
            num += 1
            sum += j["value"]

            print(sum)

        time.sleep(1)

    avg = sum / num

    return avg


res = get_result()
print(res)



# 4700.0
