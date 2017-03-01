import urllib2

def test01():
    print 'Loading'

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                              "Chrome/49.0.2623.87 Safari/537.36",
               "Cookie" : "visid_incap_876526=dzhDIsCHQE+TLLInVLBBq8Rqq1cAAAAAQUIPAAAAAABlJIZMjIHXx20+xsUJDl0+; __cfduid=d0f1b6225a79d890e86e13bcb6554028a1483420884; wp-settings-time-26502=1483420912; _gat=1; isClose=yes; wordpress_test_cookie=WP+Cookie+check; duoshuo_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaG9ydF9uYW1lIjoiMTA4MCIsInVzZXJfa2V5IjoyNjUwMiwibmFtZSI6ImtpbmRlcnJpdmVuIn0.i_xH25Ke7R_1AQYR4yNDnzEckLPr2vKFPmweAVvhsgc; wordpress_logged_in_fd8c1e6ab34e9a3b9a19fb0876603286=kinderriven%7C1485942879%7CiwK34VP4d0VROTsMTXQ6Q8tzLVzOHS8tQUkYFW2h7oz%7Ceaa4949aa6292393bf5a8d244e12b032513fb4facb4caad384dcd269cfbfaed5; PHPSESSID=b3faqjrq0uo0917du2d6kru1h4; _ga=GA1.2.440576639.1470851775; Hm_lvt_fdf50fdc4a2f4d872461c1933304bf55=1483855835,1483880868,1484025283,1484732852; Hm_lpvt_fdf50fdc4a2f4d872461c1933304bf55=1484733291"}
    url = "http://dm1080p.com/archives/15772"
    request = urllib2.Request(headers=headers, url=url)
    response = urllib2.urlopen(request)

    print response.read()


print 'Loading...'

test01()