import urllib2
from pytesseract import *
from PIL import Image

def getCode():
	vrifycodeUrl = "********" #自己分析出验证码生成地址
	file = urllib2.urlopen(vrifycodeUrl)
	pic= file.read()
	path = "d:\\code.jpg"#这里可以自己修改
	localpic = open(path,"wb")
	localpic.write(pic)
	localpic.close()
	im = Image.open(path)
	text = image_to_string(im)
	print "---------------------------"+text
	return text
# getCode()