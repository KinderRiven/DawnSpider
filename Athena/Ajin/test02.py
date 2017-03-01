import urllib2
import urllib

def test02():

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                              "Chrome/49.0.2623.87 Safari/537.36"}
    url = "http://dm1080p.com/wp-login.php"
    data = urllib.urlencode({
            "log" : "KinderRiven",
            "pwd" : "125506",
        })

    request = urllib2.Request(headers=headers, data=data, url=url)
    response = urllib2.urlopen(request)
    print response.info()
    print response.info().getheader("Set-Cookie")


test02()