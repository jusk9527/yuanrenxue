import time
import requests
headers = {
    'Host': 'match.yuanrenxue.com',
    'Referer': 'http://match.yuanrenxue.com/match/6',
    'User-Agent': 'yuanrenxue.project',
    'X-Requested-With': 'XMLHttpRequest'
}

# express 服务调用
def get_m(timestamp, count):
    """ express 服务调用 """
    return requests.post('http://localhost:3000/encrypt', data={
        'timestamp': str(timestamp),
        'count': count
    }).text

q = ''
count = 0

all_data = []
for page in range(1, 6):
    count += 1
    timestamp = int(time.time()) * 1000
    m = get_m(timestamp,str(count))
    q += f'{str(count)}-{timestamp}|'
    params = {
        'page': page,
        'm': m,
        'q': q
    }
    print(params)
    url = 'http://match.yuanrenxue.com/api/match/6'
    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    all_data += response.json()['data']
total = 0
for each in all_data:
    num3 = int(each['value'])
    total += num3*(1+8+15)

print(total)
# 6883344

