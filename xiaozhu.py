import urllib2,urllib
import cookielib
import Cookie
import time
import random

current_milli_time = lambda: int(round(time.time() *1000))

url = "http://m.xiaozhu.com/register.html#login"
cookie = "newcheckcode=b220167ec943822c63cc2777dbccf02d;" \
         " gr_user_id=c66b0fc9-ccbf-43b6-938b-a98c59ed02a2; " \
         "showledHistory=0;" \
         " _ga=GA1.3.1016455494.1499666304; " \
         "_gid=GA1.3.1212038852.1499666304; " \
         "gr_session_id_59a81cc7d8c04307ba183d331c373ef6=cee50d7b-70ca-4a81-b654-31482ae65508;" \
         " gr_cs1_cee50d7b-70ca-4a81-b654-31482ae65508=user_id%3A10828045659; openappled=1;" \
         " OZ_1U_2283=vid=v96317757047e4.0&ctime=1499666482&ltime=1499666480"
cookie2 = "newcheckcode=b220167ec943822c63cc2777dbccf02d;" \
          " gr_user_id=c66b0fc9-ccbf-43b6-938b-a98c59ed02a2;" \
          " showledHistory=0; openappled=1;" \
          " OZ_1U_2283=vid=v96317757047e4.0&ctime=1499666518&ltime=1499666482;" \
          " _ga=GA1.3.1016455494.1499666304; _gid=GA1.3.1212038852.1499666304; haveapp=1"
cookie3 = "newcheckcode=b220167ec943822c63cc2777dbccf02d; " \
          "gr_user_id=c66b0fc9-ccbf-43b6-938b-a98c59ed02a2; " \
          "OZ_1U_2283=vid=v96317757047e4.0&ctime=1499666518&ltime=1499666482"

headers={'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
        'Connection':'keep-alive',
        'Cookie':cookie,
        'Host': 'm.xiaozhu.com'
         }
def Cookie_test():
    cookie=cookielib.FileCookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    openr=urllib2.build_opener(handler)
    #openr.addheaders(['User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'])
    res= openr.open(url)
    print "[cookie]"
    for item in cookie:
        print item.name + ':' + item.value

def login():
    cookie=Cookie.SimpleCookie()
    cookie["session"] = random.randint(1,1000000000)
    cookie["session"]["domain"] = ".baidu.com"
    print cookie.output()
def msglist():
    data={"jsonp":"msglist_callback",
          "offset":"1",
          "step":10,
          "userid":10828045659,
          "sessid":"b900821776ac8ddf8dfbffd3b6863699",
          "userId":10828045659,
          "sessId":"b900821776ac8ddf8dfbffd3b6863699",
          "jsonp":"msglist_callback",
          "timestamp":current_milli_time()+120,
          "_":current_milli_time()}
    req=urllib2.Request("https://wirelesspub.xiaozhu.com/app/xzfk/html5/500/im/talklist",
                        #data=data,
                        headers=headers)
    res = urllib2.urlopen(req,data=urllib.urlencode(data))
    #res=urllib2.urlopen("http://m.xiaozhu.com/msglist2.html",headers)
    print res.read()
msglist()
