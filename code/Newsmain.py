# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:52:33 2016

@author: tan
"""

# 总体设计一下需要哪些模块。尽量模块化编写，哪部分功能出了问题，或是要替换，找那个模块去修改就行
# 当前目标：如果给定一个刺激(运行脚本)，就能自动去爬取页面，去掉那些已经爬过的，然后对爬取的内容
# 进行情感分析，将日期、url、标题、情感得分这四个变量存储起来。将来开发网页时，搜索某个股票，就去
# 对应的股票中找到最近两天(后面要改进为准确的48小时)的相应新闻，返回日期，新闻标题，情感得分(还是仅正负？)
# 最好跟申万那个一样，有一个饼状图。
#（是否可以将内容也爬取下来，返回这两天内容的wordcloud?因为生成图需要时间，可能不能每次点击时才生成，而是
# 每晚12点生成一次）

import os
import csv

path="D:/my_projects/text_mining/stock_project"
path_code=path+'/code'
os.chdir(path_code)

import html_downloader
import html_parser
import html_contrast
import emotion_calculator
import html_outputer



#from imp import reload #python3中reload不再作为一个模块，而是作为一个函数移到标准模块imp中

class News_Main(object):
    def __init__(self):
        self.page_downloader=html_downloader.HtmlDownloader() 
        #把第一页爬下来
        self.parser=html_parser.HtmlPaser()
        #解析出网页
        self.contraster=html_contrast.HtmlContrast()
        #看上面解析的是否和以前的有重复，只返回不重复的。如果该股票不曾出现过，则创建新的文件
        self.emotion_cal=emotion_calculator.Emotion_Calculate()
        #计算情感得分
        self.outputer=html_outputer.Html_Outputer()
        #输出,感觉可以和前面的contrast放在一起，
    
    def craw(self,stock):
        try:
            page=self.page_downloader.download(stock)
            html_cont=self.parser.parse(page)
            new_cont=self.contraster.contrast(stock,path,html_cont) #返回的是array
            if len(new_cont)!=0: #可能出现没有新的
                cont_with_emotion=self.emotion_cal.calculate(new_cont,path_code) #返回带有emotion的list
                self.outputer.output(stock,path,cont_with_emotion)
                print('%s add %d news'%(stock,len(cont_with_emotion)))
            else:
                print('%s has no new news'%stock)
        except:
            print("craw %s failed！"%stock)


if __name__=='__main__': 
    #stock_list=['sh601988','sz000858'] #之后将所有代码存进文件，每次读入
    stock_code_path=r'D:\my_projects\text_mining\stock_project\code\StockCode_modify.txt'
    f=open(stock_code_path,encoding="utf-8")
    reader=csv.reader(f)
    stock_list=[line[1].lower()+line[0] for line in reader][1:]
    f.close()
    for stock in stock_list: #后面可以改为多线程？
        obj_spider=News_Main() #初始化（这个初始化是否可以放在for循环之前，然后计算情感时要读取的参数放在init里）
        obj_spider.craw(stock)
    #写入时做一次判断，是否存在这个stock的文件夹，如果没有则创建，之后可以往里面增添新的
