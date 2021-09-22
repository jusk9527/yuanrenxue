import pywasm
import time
import requests

headers = {
    "User-Agent": "yuanrenxue.project",
}

def get_m():
    timestamp = int(time.time()) * 1000
    t1 = int(timestamp / 1000 / 2)
    t2 = int(timestamp / 1000 / 2 - 51)
    vm = pywasm.load("./main.wasm")
    result = vm.exec("encode", [t1, t2])
    return f'{result}|{t1}|{t2}'



res = get_m()
print(res)
def main():
    sum_list = []
    for page in range(1, 6):
        url = f'http://match.yuanrenxue.com/api/match/15?m={get_m()}&page={page}'
        response = requests.get(url=url, headers=headers)
        for i in response.json()['data']:
            sum_list.append(i['value'])
    print(sum(sum_list))


if __name__ == '__main__':
    main()


# 219388
