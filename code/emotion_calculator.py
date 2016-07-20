# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:17:05 2016

@author: tan
"""

class Emotion_Calculate(object):
    def __init__(self):
        self.new_list=[]
    def calculate(self,news_array):       
        for item in news_array:
            if len(item[2])>20:   #之后修改
                emotion='negative'
            else:
                emotion='positive'
            item_list=list(item)
            item_list.append(emotion)
            self.new_list.append(item_list)
        return self.new_list