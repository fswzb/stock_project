# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:12:01 2016

@author: tan
"""

import urllib

class HtmlDownloader(object):
    def __init__(self):
        self.url_base='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol='
        self.page=1 #只下载第一页的40条
    def download(self,stock_code):
        self.url=self.url_base+stock_code+'&Page='+str(self.page)
        self.response=urllib.request.urlopen(self.url)
        html_cont=self.response.read()
        return html_cont