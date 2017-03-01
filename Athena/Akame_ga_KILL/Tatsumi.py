#encoding=utf-8
from bs4 import BeautifulSoup
import urllib
import urllib2
import cookielib
from Athena.Akame_ga_KILL.Akame import Akame
import re
import os
import threading

import time
#任务分发器
class Tatsumi(threading.Thread):

    #初始化进行设置的加载
    #mine: 配置类
    def __init__(self, mine, max_run = 10, debug=1, lazy=0, start_mission=0):
        threading.Thread.__init__(self)
        self.mine = mine
        self.username = mine.username
        self.password = mine.password
        self.headers = mine.headers
        self.max_run = max_run
        self.root_path = mine.root_path
        self.debug = debug
        self.lazy = lazy
        self.start_mission = start_mission

    #导入任务
    def import_urls(self, urls):
        self.urls = urls

    #模拟登陆获取cookie
    def get_cookie(self):

        url = "http://dm1080p.com/wp-login.php"

        data = urllib.urlencode({
            "log" : self.username,
            "pwd" : self.password,
        })

        #申明一个cookie容器保存cookie
        cookie = cookielib.CookieJar()

        #创建cookie的处理器
        handler = urllib2.HTTPCookieProcessor(cookie)

        #构造opener
        opener = urllib2.build_opener(handler)
        request = urllib2.Request(headers=self.headers, url=url, data=data)

        #利用构造的opener来打开网页
        response = opener.open(request)

        #将获得的cookie返回
        self.cookie = cookie

    #开始执行任务
    def run(self):

        self.get_cookie()
        urls_size = len(self.urls)
        pos = 0

        while True:

            #每次清空任务栏
            thread_list = []
            #创建线程,一次最多导入[max_run]个任务
            start_pos = pos

            for i in range(0, self.max_run, 1):
                if pos >= urls_size:
                    break
                if pos >= self.start_mission:
                    thread_list.append(Akame(self.urls[pos], self.cookie,
                                         mine=self.mine, debug=self.debug, lazy=self.lazy))
                pos = pos + 1

            end_pos = pos
            print str(start_pos) + "-" + str(end_pos)

            #开启线程
            for each in thread_list:
                each.start()

            #阻塞线程
            for each in thread_list:
                each.join()

            if pos >= urls_size:
                break

        print '[END]'