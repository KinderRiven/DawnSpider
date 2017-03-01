import urllib
import urllib2
import cookielib

def test03():
    print "test03"

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                              "Chrome/49.0.2623.87 Safari/537.36"}
    url = "http://dm1080p.com/wp-login.php"
    data = urllib.urlencode({
            "log" : "KinderRiven",
            "pwd" : "125506",
        })

    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    request = urllib2.Request(url=url, data=data, headers=headers)
    response = opener.open(request)

    print cookie

test03()