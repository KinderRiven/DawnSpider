#encoding=utf-8

import os
from bs4 import BeautifulSoup


#全局配置类
#load负责加载配置文件

#模拟登陆的账号密码
#保存路径

class Mine:

    def __init__(self):
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}
        self.load()

    def load(self):

        #读取配置文件
        f = open("setting")
        fr = f.read()

        #按节点进行读取
        soup = BeautifulSoup(fr, "html.parser")
        self.username = soup.find("username").text
        self.password = soup.find("password").text
        self.root_path = soup.find("save_path").text
        print self.username + " " + self.password + " " + self.root_path

    def load_list(self):
        f = open("setting")
        fr = f.read()

        soup = BeautifulSoup(fr, "html.parser")
        dm_list = soup.find_all("item")

        ret_list = []
        for each in dm_list:
            ret_list.append(str(each.find("url").text))
        print len(dm_list)

        return  ret_list

mine = Mine()
mine.load_list()