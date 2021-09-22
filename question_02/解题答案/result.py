import requests
import execjs
import time

# burp0_url = "https://match.yuanrenxue.com:443/api/match/2"
# burp0_cookies = {"Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1628841103,1628849363,1629358342,1629445685",
#                  "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1628841107,1628849371",
#                  "m": "39ae10ef34689d9273f6f843e4264032|1629448307000",
#                  "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1629448317"}
# burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
#                  "Accept": "application/json, text/javascript, */*; q=0.01",
#                  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#                  "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Connection": "close",
#                  "Referer": "https://match.yuanrenxue.com/match/2", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors",
#                  "Sec-Fetch-Site": "same-origin", "Cache-Control": "max-age=0"}
# res = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
#
#
# print(res.text)




file = "./get_m.js"


def get_result():
    sum = 0
    ctx = execjs.compile(open(file).read())
    res = ctx.call('get_m')

    m = res + "|"+str(int(time.time())*1000)

    for i in range(1, 6):
        burp0_cookies = {"Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1628841103,1628849363,1629358342,1629445685",
                         "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1628841107,1628849371",
                         "m": "{0}".format(m),
                         "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1629448317"}
        burp0_headers = {
            'User-Agent': 'yuanrenxue.project',
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Connection": "close",
            "Referer": "https://match.yuanrenxue.com/match/2", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin", "Cache-Control": "max-age=0"}

        burp0_url = "https://match.yuanrenxue.com:443/api/match/2?page={0}".format(i)

        response = requests.get(burp0_url, headers=burp0_headers,cookies=burp0_cookies).json()

        for j in response.get('data'):
            sum += j["value"]
        time.sleep(1)

    return sum


res = get_result()
print("结果为"+str(res))
# 结果为248974
