
import requests
import re
import base64
from urllib.parse import urlencode
SUM_TOTAL_LIST = []
CHARACTERS_NUM_MAP = {
    '1': 155,
    '2': 166,
    '3': 175,
    '4': 456,
    '5': 436,
    '6': 446,
    '7': 725,
    '8': 766,
    '9': 776,
}

def get_click_characters_and_image(session, page):
    """
    认证文字和图片
    :param session:
    :param page:
    :return:
    """
    image_url = 'http://match.yuanrenxue.com/api/match/8_verify'
    with session.get(url=image_url) as response:
        if response.status_code == 200:
            image_pattern = re.compile(r'<img src=.*?base64,(.*?)\" alt=', re.S)
            click_characters_pattern = re.compile(r'<p>(.*?)</p>', re.S)
            click_unicode_characters = re.findall(click_characters_pattern, response.text)
            click_characters = list(map(lambda x: x.encode('utf-8').decode('unicode-escape'), click_unicode_characters))
            image_base64_str = image_pattern.findall(response.text)[0] if image_pattern.findall(response.text) else ''
            if image_base64_str:
                with open(f'{page}_origin.png', 'wb') as f:
                    f.write(base64.b64decode(image_base64_str))

            return click_characters



def get_one_page(session, page):
    click_characters = get_click_characters_and_image(session, page)
    print(click_characters)
    nums = input('请在处理后的图片中依次输入文字占位号：')
    temp_list = []
    for num in nums:
        temp_list.append(str(CHARACTERS_NUM_MAP.get(num)))
    query_string = {
        'page': page,
        'answer': '|'.join(temp_list) + '|'
    }
    dst_url = 'http://match.yuanrenxue.com/api/match/8?' + urlencode(query_string)
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                print(f'第{page}页数据为：', res.get('data'))
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def main():
    session = requests.Session()
    headers = {
        'Host': 'match.yuanrenxue.com',
        'User-Agent': 'yuanrenxue.project',
        'Referer': 'http://match.yuanrenxue.com/match/8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.104 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    session.headers = headers
    for page in range(1, 6):
        get_one_page(session, page)

if __name__ == '__main__':
    main()
