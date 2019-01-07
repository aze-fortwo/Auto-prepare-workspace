#coding:utf-8

import tkinter as tk
import time
import os

def makeApp(self):

	#==============PYTHON=============
	def makePyFile():
		self.name.grid(row=0,column=1)
		self.nameLabel.config(text='File Name:')
		self.nameLabel.grid(row=0,column=0)
		self.createButton.config(command=createPyFile)
		self.createButton.grid(row=0,column=3)

	def createPyFile():
		pyFile = self.name.get() + '.py'
		with open(pyFile,'w+', encoding='utf-8') as ofi:
			local = time.localtime()
			current_time = "#------" + str(local.tm_mday) +'/'+ time.strftime('%B') +'/'+ str(local.tm_year) +\
							'  ' + str(local.tm_hour) +':'+ str(local.tm_min) +':'+ str(local.tm_sec) + '------\n\n'			
			ofi.write(current_time)
			ofi.write('#encoding:utf-8\n\nprint(\'Hello World\')')

	def makePyProject():
		self.name.grid(row=0,column=1)
		self.nameLabel.config(text='Project Name:')
		self.nameLabel.grid(row=0,column=0)
		self.createButton.config(command=createPyFold)
		self.createButton.grid(row=0,column=3)

	def createPyFold():
		os.mkdir(self.name.get())
		fileName = self.name.get() + '\\' + self.name.get()+'.pyw'
		with open(fileName,'w+',encoding='utf-8') as ofi:
			local = time.localtime()
			current_time = "#------" + str(local.tm_mday) +'/'+ time.strftime('%B') +'/'+ str(local.tm_year) +\
							'  ' + str(local.tm_hour) +':'+ str(local.tm_min) +':'+ str(local.tm_sec) + '------\n\n'			
			ofi.write(current_time)
			ofi.write('#encoding:utf-8\n\nprint(\'Hello World\')')

	#===============HTML=================

	def makeHTMLFile():
		self.name.grid(row=0,column=1)
		self.nameLabel.config(text='File Name:')
		self.nameLabel.grid(row=0,column=0)
		self.createButton.config(command=createHTMLFile)
		self.createButton.grid(row=0,column=3)


	def makeCSSFile():
		self.name.grid(row=0,column=1)
		self.nameLabel.config(text='File Name:')
		self.nameLabel.grid(row=0,column=0)
		self.createButton.config(command=createCSSFile)
		self.createButton.grid(row=0,column=3)

	def createHTMLFile():
		HTMLFile = self.name.get() + '.html'
		with open(HTMLFile,'w+', encoding='utf-8') as ofi:
			local = time.localtime()
			current_time = "<!------" + str(local.tm_mday) +'/'+ time.strftime('%B') +'/'+ str(local.tm_year) +\
							'  ' + str(local.tm_hour) +':'+ str(local.tm_min) +':'+ str(local.tm_sec) + '------>\n\n'			
			ofi.write(current_time)
			ofi.write('<!DOCTYPE: html>\n<html>\n\t<head>\n\t<meta charset=\'utf-8\'>\n\t</head>\n\t<body>\n<div id="bloc_page">\t<header></header>\n\t\t<footer></footer>\n\t</body>\n</html>')
	
	def createCSSFile():
		CSSFile = self.name.get() + '.css'
		with open(CSSFile,'w+', encoding='utf-8') as ofi:
			local = time.localtime()
			current_time = "/*------" + str(local.tm_mday) +'/'+ time.strftime('%B') +'/'+ str(local.tm_year) +\
							'  ' + str(local.tm_hour) +':'+ str(local.tm_min) +':'+ str(local.tm_sec) + '------*/\n\n'			
			ofi.write(current_time)

	def makeHTMLProject():
		self.name.grid(row=0,column=1)
		self.nameLabel.config(text='Project Name:')
		self.nameLabel.grid(row=0,column=0)
		self.createButton.config(command=createHTMLFold)
		self.createButton.grid(row=0,column=3)

	def createHTMLFold():
		os.mkdir(self.name.get())
		HTMLfileName = self.name.get() + '\\' + self.name.get() + '.html'
		with open(HTMLfileName,'w+', encoding='utf-8') as ofi:
			local = time.localtime()
			current_time = "<!------" + str(local.tm_mday) +'/'+ time.strftime('%B') +'/'+ str(local.tm_year) +\
							'  ' + str(local.tm_hour) +':'+ str(local.tm_min) +':'+ str(local.tm_sec) + '------>\n\n'			
			ofi.write(current_time)
			ofi.write('<!DOCTYPE: html>\n<html>\n\t<head>\n\t\t<meta charset=\'utf-8\'>\n\t\t<link rel="stylesheet" url=".css">\n\t</head>\n\t<body>\n\t\t<div id="bloc_page">\n\t\t\t<header></header>\n\t\t\t<footer></footer>\n\t\t</div>\n\t</body>\n</html>')

		CSSfileName = self.name.get() + '\\' + self.name.get() + '.css'
		with open(CSSfileName,'w+', encoding='utf-8') as ofi:
			current_time = "/*------" + current_time[2:-2] +'*/\n'
			ofi.write(current_time)


#==============TOP-MENU=============
	self.menubar = tk.Menu(self)
	self.python = tk.Menu(self.menubar, tearoff=0)
	self.python.add_command(label='New Python Project', command=makePyProject)
	self.python.add_command(label='New Python File', command=makePyFile)
	self.python.add_separator()
	self.python.add_command(label='Project/File Info')
	self.menubar.add_cascade(label='Python', menu=self.python)

	self.Web = tk.Menu(self.menubar,tearoff=0)
	self.Web.add_command(label='New HTML-CSS Project', command=makeHTMLProject)
	self.Web.add_command(label='New HTML File', command=makeHTMLFile)
	self.Web.add_command(label='New CSS File', command=makeCSSFile)
	self.Web.add_separator()
	self.Web.add_command(label='Project/File Info')
	self.menubar.add_cascade(label='HTML', menu=self.Web)

	self.config(menu=self.menubar)

	self.name = tk.Entry(app)
	self.nameLabel = tk.Label(self, text='')
	self.createButton = tk.Button(self, text='+')

app = tk.Tk()

app.title('NEW CODE')
makeApp(app)



app.mainloop()


