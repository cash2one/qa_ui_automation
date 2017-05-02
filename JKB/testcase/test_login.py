#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：定义loginTest类，用于测试登录功能
'''
import sys,os
if ".." not in sys.path:
    sys.path.append("..")
JKBDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# 获取项目目录
proDir = os.path.abspath(os.path.join(JKBDir, os.pardir))
sys.path.append(proDir)
# pageHandler目录
pageHandlerDir =  os.path.join(proDir, "pageHandler")
sys.path.append(pageHandlerDir)
# page_obj目录
page_objDir =  os.path.join(proDir, "page_obj")
sys.path.append(page_objDir)
# #     '''获取项目目录'''
# project_dir =str(os.path.dirname(os.path.dirname(__file__)))
# #     '''page_obj'''
# file_path = project_dir + "/page_obj"
# sys.path.append(file_path)
from time import sleep
import unittest
from pageHandler.myunit import MyTest
from tools.TestRunner import TestRunner
from JKB.page_obj.loginPage import Login
# from JKB.page_obj.loginPage import Login
class loginTest(MyTest):
    '''监控宝登录 测试'''  
    @unittest.skip('暂忽略此用例')
    def test_login1(self):
        '''用户名、密码为空登录'''
        login = Login(self.browser_driver)
#         print login.login_email_xpah
        login.user_login("","")
        self.assertEqual(login.login_err_msg(),"请填写邮箱")
        self.browser_driver.insert_img('error__login1_msg')
    def test_login2(self):
        '''密码错误登录'''
#         pass
        login = Login(self.browser_driver)
#         print login.login_err_msg()
        login.user_login("rita@163.com","222")
        sleep(5)
        self.assertEqual(login.login_err_msg(),"密码不正确")
        self.browser_driver.insert_img('error_login2_msg')        
# 构造测试集
def suite():
    suite = unittest.TestSuite()
#     suite.addTest(TestSiteMonitorSmoke("test_002_get_site_monitorPoint_list"))
    suite.addTest(loginTest("test_login2"))

    return suite
# 测试
if __name__ == "__main__":
#     pass
    unittest.main(defaultTest = 'suite')
#     runner = TestRunner()
#     runner.run()        
    
        
        
        
