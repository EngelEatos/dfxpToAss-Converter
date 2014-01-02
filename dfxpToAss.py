__author__ = 'EngelEatos'
#!/usr/bin/python

##imports##
import os.path, timeit
import sys, getopt
from HTMLParser import HTMLParser
###Declarations#######
myattr=[]
text=[]
mycontent = []
source = '391673657002_704864433002_saoee.dfxp'
header_path = 'header.txt'
target='new_ass.ass'
######################

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
			tmp = str(attr).split(', ')[1].translate(None,"')")
			myattr.append(tmp)

    def handle_data(self, data):
        text.append(str(data).replace('	',''))

###initialize parser###
parser = MyHTMLParser()

##required Functions##
def find(content,i):
	index = content.find("<p", i)
	end_ = content.find("</p>", index)
	if end_ == -1:
		return -1
	mycontent.append(content[index:end_])
	return end_

def _header():
	header = read_file(header_path, 'r')
	with open(target, 'w') as myfile:
		myfile.write(header + "\n")

def _write():
	content = ("Dialogue: 0," + str(myattr[0][0:len(myattr[0])-1]) + "," + str(myattr[1][0:len(myattr[1])-1]) + ",Main Dialog,,0,0,0,," + text[0][1:len(text[0])]).rstrip() + '\n'
	with open(target, "a") as myfile:
		myfile.write(content)

def lists_clear():
	del myattr[:]
	del text[:]

def filter():
	print 'Write to file...'
	_header()
	for con in mycontent:
		parser.feed(con)
		_write()
		parser.reset()
		lists_clear()

def check_for_file():
	if os.path.isfile(target):
		os.remove(target)

def read_file(path,mode):
	handle = open(path, 'r+')
	if mode=='r':
		result = handle.read()
		handle.close()
		return result
	elif mode=='c':
		result = len(handle.readlines())
		handle.close
		return result
	elif mode=='w':
		result = len(handle.read())
		handle.close
		return result
	else:
		handle.close()
		print 'Error: Wrong Mode - ' + str(mode)

def copyright():
	print 'Coded by ' + __author__
def initial():
	check_for_file()
	
	_ass=read_file(source, 'r')
	####
	i=0
	end_=0
	now_count = 0
	####
	
	line_count = len(read_file(source, 'r'))
	
	while i <= line_count:
		if end_ == -1:
			break
		now_count = end_
		print 'Extracting Paragraph - char ' + str(i) + ' to char ' + str(now_count)
		i = now_count
		end_ = find(_ass, now_count)
		if end_ == -1:
			i = int(line_count+1)
	else:
		filter()
		print 'finish'
	return

###StartProgramm###

initial()
copyright()
