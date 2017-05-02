# -*- coding:utf-8 -*-
import sys
if ".." not in sys.path:
    sys.path.append("..")
from pageHandler.myunit import MyTest
from pageHandler.handler import Pyse
from time import sleep
import unittest
from tools.TestRunner import TestRunner

class BaiduTest(MyTest):
    def baidu_search(self,search_key):
        ''' baidu search key : pyse '''
#         self.open(url)
#         self.driver.open("https://www.baidu.com")
        self.dr.open_homPage()
        self.dr.clear("id=>kw")
        self.dr.type("id=>kw", search_key)
        self.dr.click("css=>#su")
        self.assertTrue(search_key,self.dr.get_title())
    def test_baidu1(self):
        ''' baidu search key : pyse '''
        search_key = "pyse"
        self.baidu_search(search_key)
#         self.user_login()
#     def user_login(self,username="rita@163.com",password="123456"):   
#         self.dr.open_homPage()
#         self.dr.click("xpath=>" + "//*[@id='dropdown-signin']")
#         self.dr.type("xpath=>"+".//*[@id='email']",username)
# #         self.login_text()
# #         self.login_username(username)
# #         self.login_password(password)
# #         self.login_button()
# #     def test_jkb(self):
# #         ''' 登录成功 '''
# #         self.user_login()
if __name__ == '__main__':
# #     s=JkbTest()
# #     s.jkb_login('ff', 'jkb_qa')
#     m= BaiduTest()
#     m.test_baidu1()
    runner = TestRunner()
    runner.run()
    
