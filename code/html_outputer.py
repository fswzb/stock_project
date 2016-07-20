# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:18:06 2016

@author: tan
"""
import csv

class Html_Outputer(object):
    def __init__(self):
        pass
    def output(self,stock_code,path,new_list):
        new_list.reverse() #倒序输出，最新的放在最后
        path_new=path+'/file/%s.csv'%stock_code
        f = open(path_new,"a+",encoding='utf-8')
        writer = csv.writer(f, dialect = "excel")
        writer.writerows(new_list)
        f.close()
       