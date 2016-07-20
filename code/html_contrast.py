# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:16:15 2016

@author: tan
"""
import csv
import numpy as np

class HtmlContrast(object):#比较后，变为reverve返回。在emotion计算里，采用循环计算emotion再append进列表
    def __init__(self):
        self.new=[]
    def contrast(self,stock,path,content):
        path_new=path+'/file/%s.csv'%stock
        f=open(path_new,"r+",encoding='utf-8')
        f_csv = csv.reader(f)
        history=[a for a in f_csv if len(a)>0]   #这样就把所有的读入了,因为含有空格行，得删去
        f.close()
        hist_array=np.array(history)[-40:,] #选择后40个
        new_array=np.array(content)
        self.new=new_array[-np.in1d(new_array[:,0],hist_array[:,0])]
        return self.new

       
        
        
        
# 矛盾：要续写，指针只能落在最后，不知道用什么方式能刚好回溯40个读入
# 如果想刚好读入前40个为最新，那么就要有办法能在写入时从从前面写，也没找到

        
#如果还是找不到合适的方式，两个解决方式：
#1)先试一下把全部读入？数据多了匹配也耗时，两千个股票就很多
#2)把一个股票放进一个文件夹中，每天的新闻放进一个文本里。这样当天运行时(每天一次)，新的新闻最早是昨天的,
#把昨天的文件打开，存入新的，以及创建一个新的文件存放今天的。但这太麻烦了，搜索和打开文件本身可能也需要时间
        
# csv包中可以将数据以字典形式读入，这个好！
        
        
# 还是用csv完全读入吧。只不过选择最后40项做比较，减少比较时间，读入文件的大小可能差异并不大，除非后面加入内容进入
# 新的写入按照时间排序。越新的排在越后面
        
# 读入时用列表，然后转成Numy数组来选择第1列url，数组选择的新的再转成list，写入csv
# bb[-numpy.in1d(bb[:,0],aa[:,0])] 返回bb中不在aa中的元素