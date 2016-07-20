# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:13:52 2016

@author: tan
"""
import bs4
import re

class HtmlPaser(object):
    def __init__(self):
        pass
    def parse(self,html_cont):
        self.soup=bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        heads=self.soup.find_all('div',class_='datelist')[0].find_all('a',target="_blank")
    # 要有[0]才能继续find_all,否则格式不对。
        page_total=[]
        for head in heads:
            content=head.get_text()
            link=head['href']
            try:     #为了稳健，万一再哪里出什么幺蛾子，只能这一条不要，其他不出状况的要留下来  
                m=re.match(r'http://finance.sina.com.cn(\S*)/(\d{4}).?(\d{2}).?(\d{2})/(\S+).shtml',link) #匹配日期
        #老一点的页面日期是像20151119这样的,新的是2016-03-19这样的    
        # 直接匹配日期的数字，'.'表示匹配任意除了‘\n’以外的其他字符，?表示匹配0次或1次，d后{i}中数字表示匹配i次         
                split=m.groups()
                date=split[1]+'-'+split[2]+'-'+split[3]
                page_total.append([link,date,content])              
            except:
                print("日期match出错："+link)
        return page_total