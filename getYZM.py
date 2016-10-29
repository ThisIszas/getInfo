import urllib2
from pytesseract import *
from PIL import Image
import time
def getCode():
    try:
        vrifycodeUrl = "http://218.7.49.53:9003/validateCodeAction.do?random="
        file = urllib2.urlopen(vrifycodeUrl)
        pic= file.read()
        path = "C:\\temp\\code.jpg"
        localpic = open(path,"wb")
        localpic.write(pic)
        localpic.close()
        try:
            im = Image.open(path)
            text = image_to_string(im)
            # print "---------------------------"+text
            return text
        except:
            s = "0000"
            return s
    except Exception as e:
        print e
        time.sleep(100)
        return "0000"
	# try:
	# 	im = Image.open(path)
	# 	text = image_to_string(im)
	# 	#print "---------------------------"+text
	# 	return text
	# except:
	# 	s="0000"
	# 	return s
# getCode()
