# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:18:16 2016

@author: tan
"""

import urllib
import bs4
import re
import csv
import random

"""下面的是最初尝试，但被弃用的

def sparse(soup):
    pattern=r'http://finance.sina.com.cn/(\S+)/doc(\S+).shtml' #S表示非空白字符，+表示后面可能不止一个
    heads=soup.find_all('a',target="_blank",href=re.compile(pattern))
    page_total=[]
    for head in heads:
        content=head.get_text()
        link=head['href']
        m=re.match(r'(\S+)/(\d+)-(\d+)-(\d+)/(\S+)',link) #匹配日期
        split=m.groups()
        date=split[1]+'-'+split[2]+'-'+split[3]
        page_total.append([date,content])
    return page_total
# 爬到后面的那些网页上，url中不含有'doc'了.需要再改解析规则。好像是2015-12-15号前的不是这个规律
# 可否按照属于不同子节点这个规则来？div[@class = ′datelist′]下面ul的a选项

    """

def sparse(soup):
    heads=soup.find_all('div',class_='datelist')[0].find_all('a',target="_blank")
    # 要有[0]才能继续find_all
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
            if(random.random()<0.5):#先产生随机数，后面掌握了方法再改
                emotion='positive'
            else:
                emotion='negative'
            page_total.append([link,date,content,emotion])              
        except:
            print("日期match出错："+link)
    page_total.reverse()
    return page_total

# 4000条中只有一条极为特殊的出错，可以不管。


#中国银行和五粮液的代码，之后添加更多，还要包括公司名字，或许需要变个数据类型
symbol_set=['sh601988','sz000858']
page_size=range(0,50) #每个暂且下载50页

url_base='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol='

for symbol in symbol_set:
    total=[]
    count=1
    for i in page_size:
        try:
            url=url_base+symbol+'&Page='+str(len(page_size)-i) #倒着写
            response=urllib.request.urlopen(url)
            html_cont=response.read()
            soup=bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
           # date,headline=sparse(soup)
            total+= sparse(soup)
            count+=1
            print("craw %s %d news"%(symbol,count*40)) #每页有40条
        except:
            print("craw failed")
    create_csv = open(r'C:\Users\tan\Desktop\text_mining\project\%s.csv'%symbol,"a+",encoding='utf-8')
# a+表示文件打开时会是追加模式的读写，不会覆盖原文件
# 发现写出的文件有多余空格行，网上查是说要用二进制打开，比如wb+,ab+，但是这里使用csv.writer的写入形式似乎不接受这种
    create_writer = csv.writer(create_csv, dialect = "excel")
    #create_writer = csv.writer(create_csv)
    create_writer.writerows(total) #row表示写一行
    create_csv.close()


"""
之后如果爬其他地方可能会遇到以下问题：
1）需要登录或cookie等其他信息
2）不能操作太频繁，需要sleep等，否则可能被封ip
3）如果sleep，可能会太慢，需要多线程
"""    

"""
董学姐使用到的词典包括：（1）台湾大学研发的中文情感极性词典 NTUSD；（2）知网发布的“情感分析用词语
集”；（3）搜狗拼音输入法中提供的关于财经、金融、股票、品牌等方面的词库。
其中前两个词库主要用于情感分类，而第三个词库则用于分词。
"""


"""
孔潇情感字典：使用现成的：知网情感词典和长江证券金融情感词典。其中后者的金融情感词典词库不到50个词
总结：
1）分词，使用jieba，但同时需要研究怎么扩充词库，加入金融词汇
2）情感分析，使用知网的和长江证券的词典吧。
3）需要做两个东西：y为情感正负0或1来看分类准确性，y为情感得分用来做之后的股价预测
"""

    
# 这里学到一个东西：在open时如果选择’gbk‘,在windows系统下excel默认的打开方式就不会出现乱码，
# utf-8的话，写文件时编码不会错粗，记事本能正确打开，但是excel打开是乱码，不知道excel怎么改解码方式
# 但是有时候gbk还是会报错，有些东西它编码不了，不知道是什么.


    #file=open(r'C:\Users\tan\Desktop\text_mining\project\%s.txt'%symbol,'w',encoding='utf-8')
    #for item in total:
      #  file.write("日期:%s"%item[0])
        #file.write("  标题:%s\n"%item[1])
   # file.close()
# 先暂时存储在文件夹中，不同公司为一个文件夹，每天的信息存在一个txt中，设置特定格式来存放不同新闻内容


        
# 后面看一下董学姐传的别人的代码，看看怎么组织解析出的东西，以什么样的方式存起来。
# 或许我应该直接上数据库，Mysql或者MongoDB

