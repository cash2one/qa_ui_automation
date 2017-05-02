# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：启动各种浏览器：Firefox， Chrome， IE
'''
from selenium import  webdriver
import os,time
print "开始"
print "......"
class BrowserDriver:
    def startFirefox(self):
        '''启动安装在默认位置的Firefox浏览器，并自动转到网站首页 '''
#     driver = webdriver.Firefox()
# 实例化一个驱动类
        profiledir = webdriver.FirefoxProfile(r"/Users/sunying/Library/Application Support/Firefox/Profiles/sr6smerq.default")
# 打开火狐浏览器
        self.driver = webdriver.Firefox(profiledir)
#     driver.get("http://qiye-qa.jiankongbao.com")
#     driver.quit()
        return self.driver
    def startFirefoxWithSpecificLocation(self):
        ''' 启动Firefox浏览器，并自动转到网站首页,启动Firefox浏览器需要指定驱动的位置'''
#         '''启动安装在 非 默认位置的Firefox浏览器，并自动转到网站首页'''
        firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
        os.environ["webdriver.firefox.bin"] = firefoxBin
        driver = webdriver.Firefox()
        driver.get("http://qiye-qa.jiankongbao.com")
    def startChrome(self):
        ''' 启动Chrome浏览器，并自动转到网站首页,启动Chrome浏览器需要指定驱动的位置'''
        chrome_driver = os.path.dirname(os.path.dirname(__file__)) +'/packages/chromedriver_x64.exe'
        print (str(chrome_driver))
        os.environ["webdriver.chrome.driver"] = chrome_driver
        driver = webdriver.Chrome(chrome_driver)
        driver.get("http://qiye-qa.jiankongbao.com")
    if __name__ == '__main__':
        startFirefox()
#     dr = startFirefox()
#     dr.get("http://qiye-qa.jiankongbao.com")
#     time.sleep(2)
#     dr.quit()
