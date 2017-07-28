import httplib
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " \
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

try:
    print "[Start]"
    conn = httplib.HTTPSConnection("www.airbnbchina.cn")
    conn.request("GET", "/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh"
                        "&listing_id=17536629&month=6&year=2017&count=3&_format=with_conditions",headers=headers)
    res = conn.getresponse()
    data = res.read()
   # conn.request("GET", "www.airbnbchina.cn/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh&listing_id=17536629&month=6&year=2017&count=3&_format=with_conditions",headers=headers)
    print data
except Exception as e:
    print e
