# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：定义MyTest()类，用于集成unittest.TestCase类，因为所有类都要使用setUp()和tearDown()方法
'''
import sys
if ".." not in sys.path:
    sys.path.append("..")
from selenium import webdriver
import unittest
import os
from handler import Pyse
class MyTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
    
    def setUp(self):
#         pass
#         print "begin....."
        self.browser_driver= Pyse("ff",'jkb_qa')
#         self.dr.open_homPage()()
#         print driver.homepage_url
#         driver.open(driver.homepage_url)
#         self.dr.wait(10)
#         self.driver.maximize_windows()
#     @classmethod
#     def teardown_class(self):
    def tearDown(self):
        self.browser_driver.quit()
#         print "over....."
if __name__ == '__main__':
    pass