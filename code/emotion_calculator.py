# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:17:05 2016

@author: tan
"""
import csv
import jieba
import numpy as np

class Emotion_Calculate(object):
    def __init__(self):
        self.new_list=[]
    def parse(self,text):
        words=[]
        seg_list=jieba.cut(text,cut_all=False)
        #stopwords = [line.rstrip() for line in open(path+'stopwords.txt')]这时不需要看是否在停用词中了，只要dic中没有
        for word in seg_list:
            if len(word)>1  and (not word[0].isdigit()) \
            and (not word[1].isdigit()): #去掉数字和长度小于1的词（会不会一个词都不剩下了？）
                words.append(word)
        return words
    def transword2vec_bag(self,words,dictionary):
        vec=[0]*len(dictionary) #可以直接乘积
        for word in words:
            if word in dictionary:
                vec[list(dictionary).index(word)]+=1
        return vec
    def nbclassify_bag(self,newvec,theta_neg,theta_neu,theta_pos,p_neg,p_neu,p_pos):
        px_neg=sum(newvec*np.log(theta_neg))+np.log(p_neg) #避免过小的数乘积导致下溢出
        px_neu=sum(newvec*np.log(theta_neu))+np.log(p_neu)
        px_pos=sum(newvec*np.log(theta_pos))+np.log(p_pos)
        if max(px_neg,px_neu,px_pos)==px_neg:
            label='negative'
        elif max(px_neg,px_neu,px_pos)==px_neu: 
            label='neutral'
        else:
            label='positive'
        return label
    def calculate(self,news_array,param_path): #参数和code存储在同一个文件夹,后面还要修改为，将新闻内容也放进去
        f1 = open(param_path+'/dic_parameters.csv',encoding='utf-8')
        f2 = open(param_path+'/prior.csv',encoding='utf-8')
        reader1=csv.reader(f1)
        reader2=csv.reader(f2)
        dic_param=[line for line in reader1 if len(line)>1]
        dic=[line[0] for line in dic_param] #字典词汇
        length=len(dic)
        param=np.array(dic_param)[:,1:4].astype(np.float64) #各个类别参数，先后是neg,neu,pos
        prior=np.array([line for line in reader2 if len(line)>1][0]).astype(np.float64)
        for item in news_array:
            words=self.parse(item[2])
            vec=self.transword2vec_bag(words,dic)
            emotion= self.nbclassify_bag(vec,param[:,0],param[:,1],param[:,2],prior[0],prior[1],prior[2])
            item_list=list(item)
            item_list.append(emotion)
            self.new_list.append(item_list)
        return self.new_list