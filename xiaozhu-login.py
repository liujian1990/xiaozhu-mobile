import urllib,urllib2
import cookielib
import hashlib
import random

import datetime
import time
current_milli_time = lambda: int(round(time.time() * 1000))
cj = cookielib.CookieJar()

urlroot   = 'http://mobile.xiaozhu.com/html5/'
urlimroot =  'http://imserver.xiaozhu.com:8080/webim/pushlet.srv'
urltalkMsg= 'https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/im/talkMsg'
urllogon="https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/user/login4pwd"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " \
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# headers['Access-Control-Allow-Credentials']='true'
# headers['Access-Control-Allow-Headers']='x-requested-with,content-type,Cache-Control,Pragma,Date,x-timestamp'
# headers['Access-Control-Allow-Methods']='POST, GET, OPTIONS'
#headers['Connection']="keep-alive"
#headers['Content-Type']="text/plain; charset=utf-8"
headers['content-encoding']='gzip'
headers['accept-encoding']='gzip, deflate, sdch, br'
headers['accept-language']='zh-CN,zh;q=0.8'
headers['referer']='http://m.xiaozhu.com/msglist2.html'
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders[0] = ('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " \
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
def openTalkMsg():
    data=urllib.urlencode(  )
    #req = urllib2.Request(urltalkMsg,data,headers)
    res = opener.open(urltalkMsg,data,headers)
    print res.read()

def openMsgList():
  #  opener.addheaders[0]=('User-Agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " \
  #                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    res = opener.open("http://m.xiaozhu.com/msglist2.html")
    print res.read()
def login():
    #timestamp=str(time.time())[0:10]+'120'
    timestamp=str(current_milli_time()+120)
    code='servicename=user/login4pwdsign=xiao_!@&^~&html5*_zhu_121210timestamp='+timestamp
    sign=hashlib.md5(code).hexdigest()
    randomCode=random.random()
    data = urllib.urlencode({'jsonp':"login_callback",
                            "userName":"18513848627",
                            "password":"lj3322650",
                            "nationCode":"86",
                            "nationName":"CN",
                            "uniqueId":"",
                            "imageCode":"",
                            "openId":"",
                            "companyCode":"",
                            "randomCode":randomCode,
                            "timestamp":timestamp,
                            "sign":sign})
    #https: // wirelesspub.xiaozhu.com / app / xzfk / html5 / 500 / user / login4pwd
    #http: // m.xiaozhu.com / register.html
    res = opener.open("https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/user/login4pwd"+"?"+data)
    print "[2]",res.read()

#openMsgList()
res = opener.open("http://m.xiaozhu.com/register.html")
print "[1]",res
for item in cj:
    print 'Name = '+item.name
    print 'Value = '+item.valueopenMsgList()
login()

    # jsonp:login_callback
# userName:18513848627
# password:liujian33
# nationCode:86
# nationName:CN
# uniqueId:
# imageCode:
# openId:
# companyCode:
# randomCode:0.42306366179472144
# timestamp:1499625620881
# sign:5698360f12cc497bf5f9d62936190e5a
# _:1499622078240