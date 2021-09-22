import requests
import execjs
from parsel import Selector

def get_data(data,page,list_data):
    file = "/Users/xiao/PycharmProjects/安全/ast_study/7/html.js"
    ctx = execjs.compile(open(file).read())
    info = ctx.call('get_html',data,page)

    selector = Selector(info)
    tr_list = selector.xpath('//tr')
    for tr in tr_list:
        people_data = []
        # 名字
        name = tr.xpath('./td/span/text()')[0].extract()
        # 分数
        scroce = tr.xpath('./td/span/text()')[3].extract()
        # 胜率
        rate = tr.xpath('./td[7]/div/a/text()')[0].extract()
        # 场数
        paly = tr.xpath('./td[7]/div/a[2]/text()')[0].extract()
        people_data = [name,scroce,rate,paly]

        list_data.append(people_data)
    return data




def main():
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
    }
    list_data = []
    for page in range(1,6):

        url = "http://match.yuanrenxue.com/api/match/7?page={}".format(page)
        res = requests.get(url,headers=headers).json()

        get_data(res,page,list_data)

    # 胜率
    flag = 0
    # 名字
    name = ""
    # 位置
    positon = 0
    # 页数
    num_page = 0
    for i in list_data:
        num_page = num_page+1
        num = float(i[2].strip('%'))
        if num>flag:
            flag = num
            name = i[0]
            positon = i


    print(name)
    print(flag)
    print(positon)
    print(num_page/10)

    return name



if __name__ == '__main__':
    main()

# 撩妹界扛把子
# 90.0
# ['撩妹界扛把子', '1725', '90%', '19800场']
# 50
