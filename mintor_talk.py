import urllib2,urllib
import cookielib
import Cookie
import time
import random

current_milli_time = lambda: int(round(time.time() *1000))

url = "https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/im/talklist"

cookie = "newcheckcode=0928291d22892cffe2c70196172c575e;" \
          " gr_user_id=34828992-b32f-43f3-bf06-b7713198cc3a; " \
          "gr_session_id_59a81cc7d8c04307ba183d331c373ef6=c5b2bed0-ba03-4b08-b7cd-04e15a6dd3b7; " \
          "gr_cs1_c5b2bed0-ba03-4b08-b7cd-04e15a6dd3b7=user_id%3A10828045659"

headers={'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
        'Cookie':cookie,
        'Host': 'm.xiaozhu.com'
         }

def talklist():
    data={"jsonp":"msglist_callback",
          "offset":"1",
          "step":10,
          "userid":10828045659,
          "sessid":"b900821776ac8ddf8dfbffd3b6863699",
          "userId":10828045659,
          "sessId":"b900821776ac8ddf8dfbffd3b6863699",
          "jsonp":"msglist_callback",
          "timestamp":1501125843671,
          "_":1501125843582}
    req=urllib2.Request(url,
                        data=data,
                        headers=headers)
    res = urllib2.urlopen(req,data=urllib.urlencode(data))
    #res=urllib2.urlopen("http://m.xiaozhu.com/msglist2.html",headers)
    print res.read()
talklist()
