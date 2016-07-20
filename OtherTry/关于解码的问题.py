# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

f = open(r'C:\Users\tan\Desktop\text_mining\wordcloud_sample.txt','r')
text = f.read().decode('gbk') 
print text

# 发现用jieba分词是能出现的
words=list(jieba.cut(text,cut_all=True))
for each in words:
    print each
    
%pylab qt

a=[]
for word in words: #去掉一些单字助词和空格
    if len(word)>=1:
        a.append(word)
        
txt=r' '.join(a) 
#直接用a不行，因为WordCloud().generate要求参数是string格式，a是list
# 但是也不明白为什么这样可以变成string


wordcloud = WordCloud().generate(txt)
plt.imshow(wordcloud)


wordcloud = WordCloud(background_color="white",random_state=42,\
margin=5, width=1800, height=800,max_words=2000,max_font_size=300).generate(txt)
plt.imshow(wordcloud)
# max_font_size若不调或者太大，则某个出现最多的词可能占了整个图片很大范围
# 不调背景色的话默认为黑色

wordcloud = WordCloud(background_color="white",\
margin=5, width=1800, height=800,max_words=2000,max_font_size=60,random_state=42).generate(txt)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

'永远'.decode('utf-8') in words #True
'孟连'.decode('utf-8') in words #False
'孟'.decode('utf-8') in words #True

# 所以孟连在分词的时候被拆开了


"""
f = open(r'C:\Users\tan\Desktop\text_mining\wordcloud_sample.txt','r')
text = f.read().decode('gbk') #这里utf-8还不成功
text.encode('utf-8')
f.close()
print text


f = open(r'C:\Users\tan\Desktop\text_mining\wordcloud_sample2.txt','r')
text2 = f.read().decode('utf-8') #先另存为utf-8的格式
f.close()
print text2

f = open(r'C:\Users\tan\Desktop\text_mining\wordcloud_sample3.txt','r')
text3 = f.read().decode('gbk') #另存为unicode格式
f.close()

print text3 #可以是中文，为什么单独输出text就是unicode的样子呢

# 看到很多地方说用text.encode('gbk') 或是utf-8就可以转换，但我的还是那样啊

## 怎么回事啊！


f2=open(r'C:\Users\tan\Desktop\Andrew Ng\machine learing in action\MLiA_SourceCode\machinelearninginaction\Ch04\email\spam\3.txt')
text2=f2.read() #如果是英文，不加decode()是string格式。而前面中文不加decode，出来是乱码

wordcloud = WordCloud().generate(text2)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

英文出来的就是想要的样子
"""