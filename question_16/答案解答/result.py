import time
import requests
import os
import execjs

file = "./161.js"


def get_m(t):
    ctx = execjs.compile(open(file).read())
    res = ctx.call('btoa',t)

    return res

def main():
    sums = 0
    headers = {"User-Agent": "yuanrenxue.project", }
    for i in range(1, 6):
        t = str(int(time.time())) + '000'
        m = get_m(t)
        params = {
            "page": i,
            "m": m,
            "t": t,
        }
        response = requests.get(url="http://match.yuanrenxue.com/api/match/16", params=params, headers=headers).json()
        print(response)
        for each in response["data"]:
            sums += each["value"]
    print(sums)


if __name__ == "__main__":
    main()
    # 287383
