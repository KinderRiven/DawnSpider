import urllib2
from bs4 import BeautifulSoup

#init setting
url = "http://www.jianshu.com/c/71169ced18ac"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

host = "http://www.jianshu.com"
#auto login


#work
def work(url):
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

m_html = work(url)
m_soup = BeautifulSoup(m_html, "html.parser")
m_list = m_soup.select(".trigger-menu li a")
m_urls = []

for each in m_list:
    m_urls.append(host + str(each['href']))

for each in m_urls:

    t_html = work(each)
    t_soup = BeautifulSoup(t_html,"html.parser")
    t_list = t_soup.select(".note-list li")

    for each in t_list:
        print "======================================"
        #title = each.find("a")
        print "<<" + each.select(".title")[0].text + ">>"
        print each.select(".abstract")[0].text
        print "======================================"
