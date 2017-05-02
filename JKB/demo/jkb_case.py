# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：定义MyTest()类，用于集成unittest.TestCase类，因为所有类都要使用setUp()和tearDown()方法
'''
import sys
if ".." not in sys.path:
    sys.path.append("..")
from pageHandler.myunit import MyTest
from time import sleep
from tools.TestRunner import TestRunner
class Login1(MyTest):
    '''登录功能'''
#     元素位置
    login_text_xpath = ".//*[@id='dropdown-signin']"
    login_email_xpah = ".//*[@id='email']"
    login_password_xpah = ".//*[@id='pwd']"
    login_button_xpath = ".//*[@id='sigin_btn']"
#     username_default = MyTest().dr.usernme_default
#     password_default = MyTest().dr.password_default
    login_username_succes_xpath = ".//*[@id='zh_cn']/div[1]/div[3]/div[1]/a[2]/span[1]"
    login_err_msg_xpath = ".//*[@id='msg_container']"
    username_default = "rita@163.com"
    password_default = "123456"
#         “登录”文字
    def login_text(self):
        self.dr.click("xpath=>"+self.login_text_xpath)
#         登录用户名
    def login_username(self,username):
        self.dr.clear("xpath=>"+self.login_email_xpah)
        self.dr.type("xpath=>"+self.login_email_xpah,username)
#         登录密码
    def login_password(self,password):
        self.dr.clear("xpath=>"+self.login_password_xpah)
        self.dr.type("xpath=>"+self.login_password_xpah,password)
#         登录按钮
    def login_button(self):
        self.dr.click("xpath=>"+self.login_button_xpath)
#         登录成功
    def login_success(self):
        return self.dr.get_text("xpath=>"+self. login_username_succes_xpath)
#         用户名/密码错误提示
    def login_err_msg(self):
        return self.dr.get_text("xpath=>"+self. login_err_msg_xpath)
#         self.assertEqual(username,actual)
#         定义统一登录入口
#     def user_login(self,username=username_default,password=password_default):
    def user_login(self,username="rita@163.com",password="123456"):     
        self.dr.open_homPage()
        self.login_text()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
    def test_login(self):
        ''' 登录成功 '''
        self.user_login()
#     del user_login(self,username):
#         pass
if __name__ == '__main__':
# #     s=JkbTest()
# #     s.jkb_login('ff', 'jkb_qa')
#     m= BaiduTest()
#     m.test_baidu1()
    runner = TestRunner()
    runner.run()
    