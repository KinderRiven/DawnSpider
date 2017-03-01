#encoding=utf-8

import urllib2
from Athena.Akame_ga_KILL.Mine import Mine
from bs4 import BeautifulSoup

#拉取网站信息
class Leone:

    def __init__(self, mine):
        self.headers = mine.headers

    #获得该页面的动漫信息
    def page_get_solve(self, html, data):

        soup = BeautifulSoup(html, "html.parser")
        list = soup.select("article h2 a")
        for each in list:
            item = BeautifulSoup("<item><url></url><title></title></item>\n", "html.parser")
            item.find("url").string = each["href"]
            item.find("title").string = each.text
            data.data.append(item)

    def page_get(self, start, end):

        #获取原文件信息
        fr = open("setting", "r")
        content = fr.read()
        fr.close()

        data = BeautifulSoup(content, "html.parser")
        data.find("data").string = ""

        #拉取动漫列表
        for i in range(start, end + 1, 1):

            #debug
            url = "http://dm1080p.com/page/" + str(i)
            print "[page] 正在获取: " + url
            request = urllib2.Request(headers=self.headers, url=url)

            count = 1
            html = ""
            while True:
                print "Try (" + str(count) + ")"
                try:
                    response = urllib2.urlopen(request, timeout=10)
                    html = response.read()
                    break
                except BaseException:
                    count = count + 1

            #Solve
            list = self.page_get_solve(html, data)

        #覆盖原文件信息
        fw = open("setting", "wb")
        fw.write(str(data))
        fw.close()


mine = Mine()
leone = Leone(mine)
leone.page_get(1, 156)

f = open("setting", "r")
content = f.read()
f.close()

soup = BeautifulSoup(content, "html.parser")
list = soup.select("data item")
for each in list:
    print each
