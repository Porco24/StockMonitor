#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import itchat

webURL = 'http://xueqiu.com/S/SH600835'
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }


class Stock(object):
    def __init__(self, url):
        # self.name = name;
        # self.id = id;
        self.url=url

    # Request网页
    def download(self, url, num_retries=2):
        print('Downloading', url)
        try:
            html = requests.get(url, headers=headers)
        except requests.error.URLError as e:
            print('Download error:', e.reason)
            html = None
            if (num_retries > 0):
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    return self.download(url, num_retries - 1)
        return html

    # 获取实时股价
    def stockPrice(self, url):
        html = self.download(url).text
        soup = BeautifulSoup(html, 'lxml')
        find = soup.find(class_='stock-current')
        price = find.text
        return price

    #获取公司财务信息
    def stockReported(self):
        pass


class wechatUser(object):
    def __init__(self,name):
        user = itchat.search_friends(name=name)
        try:
            self.username = user[0]['UserName']
        except:
            print('用户不存在')




# URL='http://xueqiu.com/S/SH600835'
# SH=Stock(URL)
# print(SH.stockPrice(URL))  # 输出find获取的值

itchat.auto_login(hotReload=True)
friend = itchat.search_friends(name='ysb1997')
userName=friend[0]['UserName']
print(userName)
itchat.send('PythonSendTest', toUserName=userName)
itchat.run()