# 任务：抓取这5页的数字，计算加和并提交结果



import requests
import base64


headers = {
    'authority': 'match.yuanrenxue.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'yuanrenxue.project',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.com/match/12',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1628938993; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1628939107; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1628939107; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1628939114',
}

sum = 0
for i in range(1,6):
    m = base64.b64encode(("yuanrenxue"+str(i)).encode())
    params = (
        ('page', i),
        ('m', m),
    )
    response = requests.get('https://match.yuanrenxue.com/api/match/12', headers=headers, params=params).json()

    print(response)
    data = response.get('data')

    for j in data:
        value = j.get('value')
        sum += value


print(sum)
# 247082
