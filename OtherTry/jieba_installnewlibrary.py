# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:10:37 2016

@author: tan
"""

from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

f = open(r'C:\Users\tan\Desktop\text_mining\wordcloud_sample.txt','r')
text = f.read()
print(text)
f.close

# 发现用jieba分词是能出现的,python2和python3中这两个包用法有点差异
seg_list=jieba.cut(text,cut_all=True) #cut_all参数用来控制是否采用全模式,返回所有可能生成的词
print("Full Mode: " + "/".join(seg_list))

seg_list=jieba.cut(text,cut_all=False) #这个模式应该才是我想要用的
print("Default Mode: " + "/".join(seg_list))



seg_list=jieba.cut(text,cut_all=False)

a=[]
for word in seg_list: #去掉一些单字助词和空格
    if len(word)>1:
        a.append(word)
        
txt=r' '.join(a) #或者用r'/'.join(a)


"""
# python3的wordcloud安装失败了，再看一下
上面问题解决：原因是包内部是用C++写的，所以pip安装不了，一个方法是安装Visual studio C++才能compile
另一个方式是，有人把编译好的二进制文件上传 http://www.lfd.uci.edu/~gohlke/pythonlibs/
再pip install SomePackage.whl就可以了
"""

path='C:/Anaconda2/Lib/site-packages/wordcloud/simhei.ttf'  
# 中文字体所在地方,要有中文词库才行，否则识别不了


%pylab qt

wordcloud = WordCloud(font_path=path,background_color="white").generate(txt) 
plt.imshow(wordcloud)

u'孟连' in a #True
# 在Python3.5中，字符串前面加一个u就可以变成utf-8


# 看到最后一句分成了：“见到 台中市 长 我 就 日 了 狗 了”
# 尝试安装自己的词库来增强分词能力

jieba.load_userdict("C:/Users/tan/Desktop/text_mining/mydict.txt") #自己写的几个词

seg_list=jieba.cut(text,cut_all=False)

a=[]
for word in seg_list: #去掉一些单字助词和空格
    if len(word)>=1:
        a.append(word)
        
txt=r' '.join(a) #或者用r'/'.join(a)

# 最后一句分成了： 见到 台中市 长 我 就 日了狗了' 把“日了狗了分正确了”

# 如果只是少数几个词，可以这样：
jieba.add_word(r'日了狗') #也成功做到了这一点


# 注意分词完了后，除了前面删除的长度为1的词，还要去除停用词，停用词会对有效信息产生干扰
