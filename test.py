#爬虫原理:模拟浏览器发送请求的过程（发送请求，接收结果）
import requests
import json
from more_itertools import rstrip


def spider():
    #获取请求；
    url="http://yunhq.sse.com.cn:32041/v1/sh1/list/exchange/equity?callback=jsonpCallback33592998&select=code%2Cname%2Copen%2Chigh%2Clow%2Clast%2Cprev_close%2Cchg_rate%2Cvolume%2Camount%2Ctradephase%2Cchange%2Camp_rate%2Ccpxxsubtype%2Ccpxxprodusta%2C&order=&begin=0&end=25&_=1685330869128"
    #发送请求:使用get方法模拟浏览器发送请求，如果成功，返回一个response对象
    rep=requests.get(url)
    print(rep.text)
#对获取到字符串进行切割处理，将左右两边不要的部分切除
    data=rep.text.lstrip("jsonCallback42654643("),rstrip(")")
    print(data,type(data))
#将data转化为字典
    data=json.loads(data)
    print(data,type(data))
#循环输出data中的list键对应的值
    print(data["list"])
    for item in data["list" ]:
        print(item)

if __name__ =='__main__ ':
    spider()