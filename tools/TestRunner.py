# coding=utf-8
import time
import os
from .HTMLTestRunner import HTMLTestRunner
import unittest


class TestRunner(object):
    ''' Run test '''

    def __init__(self, cases="./",title="Auto Test Report",description="Test case execution"):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):

#         for filename in os.listdir(self.cases):
#             if filename == "report":
#                 break
#         else:
#             os.mkdir(self.cases+'/report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        '''获取上级目录'''
        base_dir =str(os.path.dirname(os.path.dirname(__file__)))
        '''截图保存'''
        file_path = base_dir + "/JKB/report/"
#         print file_path
        fp = open(file_path+ now +"result.html", 'wb')
#         fp = open("./report/"+ now +"result.html", 'wb')
        tests = unittest.defaultTestLoader.discover(self.cases,pattern='test*.py',top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)


if __name__ == '__main__':
    test = TestRunner()
    test.run()
