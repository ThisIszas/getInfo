import urllib2
from pytesseract import *
from PIL import Image

def getCode():
	vrifycodeUrl = "********" #�Լ���������֤�����ɵ�ַ
	file = urllib2.urlopen(vrifycodeUrl)
	pic= file.read()
	path = "d:\\code.jpg"#��������Լ��޸�
	localpic = open(path,"wb")
	localpic.write(pic)
	localpic.close()
	im = Image.open(path)
	text = image_to_string(im)
	print "---------------------------"+text
	return text
# getCode()