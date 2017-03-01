#encoding=utf-8
from bs4 import BeautifulSoup
import urllib
import urllib2
import cookielib
import re
import os
import threading
import time

#线程试任务执行Item

class Akame(threading.Thread):

    #初始化爬虫任务
    def __init__(self, url, cookie,  mine, debug = 1, lazy = 0):

        threading.Thread.__init__(self)
        self.url = url
        self.cookie = cookie
        self.headers = mine.headers
        self.debug = debug
        self.root_path = mine.root_path
        self.lazy = lazy
        #每次连接完成之后的延时

    #建立文件夹
    def build_folder(self):

        #建立文件夹
        title = self.title.replace("/", "")\
                .replace("\\", "")\
                .replace(":", "")\
                .replace("<", "")\
                .replace(">", "")\
                .replace("*", "")\
                .replace("?", "")\
                .replace("\"", "")\
                .replace("|", "")

        self.path = self.root_path + title + "/"

        #文件已经存在
        if os.path.exists(self.path) == False:
            os.mkdir(self.path)
            return True
        else:
            print "[Build Error] + " + title
            self.downloads = []
            return False


    def get_code(self):

        #正则提取提取下载码

        t_html = str(self.soup.find(id="article-content-single"))
        match = []

        pattern1 = re.compile('资料编号：(.*?)-')
        match1 = pattern1.findall(t_html)
        for i in range (0, len(match1), 1):
            match.append(match1[i].replace(" ", ""))

        pattern2 = re.compile('资料编码：(.*?)-')
        match2 = pattern2.findall(t_html)
        #去除空格
        for i in range (0, len(match2), 1):
            match.append(match2[i].replace(" ", ""))

        #打印该动漫的所有下载代码
        print match
        self.downloads = match


    #获得下载页面的源代码
    def   get_html(self):

        #加入cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))

        #建立request请求
        request = urllib2.Request(headers=self.headers, url=self.url)

        #打开页面
        response = opener.open(request)
        self.html = response.read()

    #提取页面内的下载信息
    def get_download_code(self):

        self.soup = BeautifulSoup(self.html, "html.parser")

        #提取标题
        self.title = self.soup.find("h2").find("a").text

        #打印动漫的标题
        print "[" + self.title + "]"

        #建立文件夹
        if self.build_folder() == False:
            return

        #提取code
        self.get_code()


    #进入下载页面获得下载文件的链接
    def get_download_html(self, url):

        #打印下载的url地址
        if self.debug == 1:
            print '================ New Mission ================'
            print "[" + url + "]"

        #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        request = urllib2.Request(headers=self.headers, url=url)

        count = 1
        html = ""

        while True:

            if self.debug == 1:
                print "Try (" + str(count) + ")"
            try:
                response = urllib2.urlopen(request, timeout=30)
                html = response.read()
                break
            except BaseException:
                count = count + 1

            if count > 10:
                break

        if count > 10:
            print "[" + url + "] 页面加载失败"
            return

        #获取文件信息
        try:
            soup = BeautifulSoup(html, "html.parser")
            f_info = soup.select("div.fileinfo_l p")
            f_name = f_info[0].text
            f_type = f_info[2].text
            f_url = soup.select("span.linkHidden a")[0]['href']
            self.download(f_name[5 : len(f_name)], f_url, f_type[5 : len(f_type)])
        except BaseException:
            print "[" + url + "] 页面信息读取错误"

    #开始下载
    def download(self, name, url, type):

        if self.debug == 1:
            print '----------------Start Download---------------'

        request = urllib2.Request(headers=self.headers, url=url)

        if self.debug == 1:
            print "NAME [" + name + "]"
            print "URL  [" + url + "]"
            print "TYPE [" + type + "]"

        count = 1

        while True:

            if self.debug == 1:
                print "Try (" + str(count) + ")"

            try:
                data = urllib2.urlopen(request, timeout=30).read()
                f = file(self.path + name + "." + type, "wb")
                f.write(data)
                f.close()
                break
            except BaseException:
                if self.debug == 1:
                    print "下载出错"
                count = count + 1

            #重连10次跳出，下载失败
            if count > 10:
                break

        if self.debug == 1:
            if count < 10:
                print "下载成功"
            else:
                print "[" + self.title + "]" + "下载失败"
            print '---------------------------------------------'

    #执行任务
    def run(self):

        self.get_html()
        time.sleep(self.lazy)

        self.get_download_code()
        time.sleep(self.lazy)

        for each in self.downloads:
            self.get_download_html("http://zzzpan.com/?/file/view-" + each + ".html")
            time.sleep(self.lazy)

