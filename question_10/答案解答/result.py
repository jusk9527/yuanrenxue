import requests
import base64
import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def gettime():
    time.sleep(1)
    return str(int(time.time()))+'000'

def main():
    # m为12位时间截，末尾增加一个0，除去最后一位后base64作为ecb的key
    # f为10位时间截，末尾增加三个0
    popularitylist = []
    m = str(int(time.time()*1000))
    f = gettime()
    data = ''
    nodejs = os.popen('node 0501 '+f)
    data += nodejs.read().replace('\n', '')+','
    nodejs.close()
    for i in range(3):
        nodejs = os.popen('node 0501 ' + gettime())
        data += nodejs.read().replace('\n', '') + ','
        nodejs.close()
    nodejs = os.popen('node 0502 '+m)
    cm = nodejs.read().replace('\n', '')
    data += cm
    nodejs.close()
    key = base64.b64encode(m[:-1].encode())
    cryptor = AES.new(key=key, mode=AES.MODE_ECB)
    data = base64.b64encode(cryptor.encrypt(pad(data.encode(), AES.block_size))).decode()
    headers = {
        'cookie': 'm='+cm+'; RM4hZBv0dDon443M='+data
    }
    for page in range(1, 6):
        url = 'http://match.yuanrenxue.com/api/match/5?page='+str(page)+'&m='+m+'&f='+f
        response = requests.get(url, headers=headers).json()
        for each in response['data']:
            popularitylist.append(each['value'])
    popularitylist.sort()
    sums = sum(popularitylist[-5:])
    print(sums)
    # 前五名总和：47313

if __name__ == '__main__':
    main()
