#!/usr/bin/python
#-*- coding: utf-8  -*- 
#测试套件，可以加入多个测试集

import unittest,doctest,os,sys
from datetime import datetime
#         项目路径
proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(proDir)
JBKDir =  os.path.join(proDir, "JKB")
sys.path.append(JBKDir)
#         report目录路径

reportPath = os.path.join(JBKDir, "report")
report_datePath = os.path.join(reportPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
from testcase import test_login
from tools import HTMLTestRunner
import shutil
reload(sys)

# sys.setdefaultencoding('utf-8')
suite = doctest.DocTestSuite  
suite = unittest.TestSuite()  
# suite.addTest(unittest.makeSuite(test_site_monitor.TestSiteMonitorSmoke))#引入测试的类，测试用例就被包含在类中  
suite.addTest(unittest.makeSuite(test_login.loginTest))
# suite.addTest(unittest.makeSuite(test_user_manage_demo. TestUserManageSmoke))
# suite.addTest(unittest.makeSuite(test_site_monitor_demo.TestSiteMonitorSmoke))
# suite.addTest(unittest.makeSuite(regWithDevice.testRegWithDevice))  
#unittest.TextTestRunner(verbosity=2).run(suite) #这是只运行，不生成报告的做法  

        # create test result file if it doesn't exist
if not os.path.exists(report_datePath):
            os.mkdir(report_datePath)
reportFile = os.path.join(report_datePath, "result.html")
fp = file(reportFile,'wb') #定义报告文件权限，wb，表示有读写权限  
runner = HTMLTestRunner.HTMLTestRunner(  
        stream = fp,  
        title ='Web-UI测试报告',  
        description = '测试用例见下表：')  
  
runner.run(suite)#执行测试  
fp.close()#关闭文件，否则会无法生成文件 
shutil.copy(reportFile,reportPath)  