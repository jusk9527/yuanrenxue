import requests
from collections import Counter

num_list = []
session = requests.session()
headers = {
    'Content-Length': '0',
    'User-Agent':'yuanrenxue.project',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-us;q=0.8,en;q=0.7',
    'Cookie':'sessionid=dsm1w443hobat4gntapws073tvby6fvm;'
}
session.headers = headers
for page in range(1, 6):
    resp = session.post('https://match.yuanrenxue.com/jssm')

    print(resp.headers)
    response = session.get(f'https://match.yuanrenxue.com/api/match/3?page={page}')

    print(response.text)
    data = response.json()["data"]
    print(data)
    for d in data:
        num_list.append(d['value'])
winner = Counter(num_list).most_common(1)[0][0]
print(f'最高频率申请号为:{0}'.format(winner))
