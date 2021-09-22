import requests
from collections import Counter

num_list = []
session = requests.session()
headers = {
    'user-agent':'yuanrenxue.project',
    'content-length': '0',
    'accept': '*/*',
    'referer': 'https://match.yuanrenxue.com/match/3',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'zh-TW,zh;q=0.9,en-us;q=0.8,en;q=0.7',
    'cookie':'sessionid=mkd0y5h364zorpr33f8uxu6ft5a0pj2l;'
}
list_num = []
session.headers = headers
for page in range(1, 6):
    resp = session.post('https://match.yuanrenxue.com/jssm')

    print(resp.headers)
    response = session.get(f"http://match.yuanrenxue.com/api/match/3?page={page}")
    print(response.json())

    for each in response.json()['data']:
        list_num.append(each['value'])
print(Counter(list_num))

print(Counter(list_num).most_common(1)[0][0])
# 8717
