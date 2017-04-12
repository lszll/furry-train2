#encoding utf-8 

import requests

def spider_for_amazon():
    url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    keyword = "Mozilla 5.0"
    try:
        kv = {"user-agent":keyword}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apprent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")

def spider_for_baidu():
    keyword = "python"
    try:    
        kv = {'wd':keyword}
        r = requests.get("http://www.baidu.com/s", params = kv)
        print(r.request.url)
        r.raise_for_status
        print(len(r.text))
    except:
        print("error!")

def spider_for_save():
    path = "E:/abc.jpg"
    
