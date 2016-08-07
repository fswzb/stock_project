# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, \
     request, url_for
import csv

app = Flask(__name__)#创建了一个Flask类的实例，告诉Flask到哪里去找应用所需的静态资源和模板。在我们的例子中，我们传递了name，让Flask在当前模块内定位资源
app.secret_key = 'some_secret'

@app.route('/')#定义了一些关于/的路由
def index():
    return render_template('index.html') #根目录下的初始网页

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'tannima' or \
                request.form['password'] != '123':
            error = 'Invalid credentials'
        else:
        	verification=True
        	username=request.form['username'] #本来想在stock函数中传入参数username，这样就可以在stock.html中的welcome后加入名字，但是失败了
        	#flash('You were successfully logged in') #如果身份验证成功，则闪现此消息
        	return redirect(url_for('stock')) #这个还要改，应该改写成查询股票代码的页面。
        	#resirect重新定向似乎就会跳出当前函数，下面的return不再执行
    return render_template('login.html', error=error) 
    #如果只是get方法，比如通过首页的login链接到达此处，或是刷新/login页面时,直接进入login.html且error为None。
    #如果输入过账号密码了则以post进入，输错了则会使得error变量变为一个非空的字符串，然后依然进入login.html(无论如何都会进入)

#verification=False
@app.route('/stock', methods=['GET', 'POST'])
def stock(): #要使得登陆后才能进入这个页面,但是现在其实可以直接到这个url不需就行身份验证，这个bug还要改正！
	"""if verification==False:
		return redirect(url_for('login'))
	else:
		return render_template('stock.html') """
	error = None
	if request.method == 'POST':
		if request.form['stockcode'] != 'sh601988': #之后需要读入包含所有股票代码的文件
			error = 'this stock does not exist, please input again'
		else:
			stockcode=request.form['stockcode']
			news=query(stockcode)
			for i in range(len(news)):
				each_news=news[i]
				#each_news2=each_news[1:].append(each_news[0]) #之后换一下顺序，把url放最后
				flash(' '.join(each_news))
	return render_template('stock.html',error=error)

def query(stockcode):
	path='D:/my_projects/text_mining/stock_project/file/'+stockcode+'.csv'
	f=open(path,"r+",encoding='utf-8')  #python2貌似不能这样读，而这里还必须采取python2，很烦躁！后来发现并不是非要用python2
	#虽然之前python默认为2且pip装在2下，但是只要用virtualenv -p /usr/bin/python3 py3env，就可以source py3env/bin/activate
	#然后在python3的虚拟空间中安装flask以及运行这个文件了(改了文件路径和IP地址)。
	f_csv = csv.reader(f)
	history=[a for a in f_csv if len(a)>0]   #这样就把所有的读入了,因为含有空格行，得删去
	f.close()
	return history[-10:]

app.debug=True
if __name__ == "__main__":
    app.run(host='127.0.0.1')
