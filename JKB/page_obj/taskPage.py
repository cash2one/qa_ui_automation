#!/usr/bin/env python
# -*- coding: utf-8 -*-
#filename: task.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from loginPage import Login
from pageHandler.myunit import MyTest

class TaskHandler(MyTest):
	def __init__(self):
		pass
#     元素位置
# 	概览-创建监控项目xpath
	create_task_xpath = ".//*[@id='zh_cn']/div[2]/a[5]"
# 	网站http-创建项目xpath
	create_site_http_xpath = ".//*[@id='main_content']/ul[1]/li[1]/div/a[1]"
# 	创建新监控项目页面-监控项目名称
	create_site_http_taskname_xpath = ".//*[@id='task_name']"
# 	创建新监控项目页面-监控项目url
	create_site_http_url_xpath = ".//*[@id='url']"
# 	创建新监控项目页面-监控项目url
	create_site_http_url_xpath = ".//*[@id='url']"	
	def search_site_task(self, taskinfo, tasktype):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择Task类型
		#self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(2) > a").click()
		#Input task keywords in search box and click search
		taskname = taskinfo['taskname']
		self.find_element_by_id("keywords").clear()
		self.find_element_by_id("keywords").send_keys(taskname)
		self.find_element_by_id("filterBotton").click()
		time.sleep(3)
		#print self.is_element_present("css selector", "#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(10)")
		if self.is_element_present("css selector", "#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(4)>a[title=%s]" %taskname):
			print "Target Task Found."
		else: print "Target Task Not Found!"
		if self.is_element_present("link text", taskname): return True
		else: return False


	def print_site_task_info(self, taskname, tasktype):
		taskname = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(4) a").text
		url = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(5) span").text
		tasktype = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(6) a").text
		frequency = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(7) span").text
		availability = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(8) span").text
		resptime = self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(9) span").text
		print "Task info: ", [taskname, url, tasktype, frequency, availability, resptime]
	
	
	
	def create_site_task(self, taskinfo, tasktype):
		print 'Task to be created: ', taskinfo
		if tasktype == 'http':
			self.create_site_task_http(taskinfo)
		elif tasktype == 'ping':
			self.create_site_task_ping(taskinfo)
		elif tasktype == 'ftp':
			self.create_site_task_ftp(taskinfo)
		elif tasktype == 'dns':
			self.create_site_task_dns(taskinfo)
		elif tasktype == 'tcp':
			self.create_site_task_tcp(taskinfo)
		elif tasktype == 'udp':
			self.create_site_task_udp(taskinfo)
		elif tasktype == 'smtp':
			self.create_site_task_smtp(taskinfo)
		elif tasktype == 'traceroute':
			self.create_site_task_traceroute(taskinfo)
	
	
	def create_site_task_basic(self, taskinfo):
		openlist = ['所有所在企业用户','用户组','部分企业用户','仅限本人']
		freqlist = ['2分钟','2分钟','5分钟','10分钟','15分钟','20分钟','30分钟','60分钟']
		remdlist = ['lab_reminds_0','lab_reminds_1','lab_reminds_2','lab_reminds_3','lab_reminds_4','lab_reminds_5','lab_reminds_6','lab_reminds_7']
		rtrylist = ['1次','1次','2次','3次']
		histlist = ['关闭','开启']
		self.find_element_by_css_selector("span.select-arrow").click()
		if taskinfo.get('class'):
			self.find_element_by_link_text(taskinfo["class"]).click()
		#self.find_element_by_link_text(openlist[taskinfo["openscope"]]).click()
		#time.sleep(3)
		self.find_element_by_link_text(freqlist[taskinfo["frequency"]]).click()
		self.find_element_by_css_selector("#reminds_ul>li:nth-of-type(%d)" %taskinfo['reminds']).click()
		self.find_element_by_link_text(rtrylist[taskinfo["retry"]]).click()
		self.find_element_by_link_text(histlist[taskinfo["history"]]).click()
		#self.find_element_by_css_selector("#group_id>option:nth-of-type(2)").click()
		es = self.find_elements_by_css_selector("#group_id>option")
		for e in es:
			#print e.get_attribute('value')
			if e.text.encode('utf-8') == '%s' %taskinfo['mongroup']:
				e.click()
		time.sleep(3)
		#点击‘创建项目’按钮来确认创建任务。
		#self.find_element_by_xpath(u"(//td[contains(text(),'rachel_wang02@163.com')])[1]").text
		#print self.is_element_present("xpath", "//td[contains(text(),'rachel_wang02@163.com')]")
		self.find_element_by_css_selector("a.btn.btn-primary > b").click()
		time.sleep(3)
	
	
	def create_site_task_http(self, taskinfo):
		#选择网站监控
		self.browser_driver.click("xpath=>" + self.create_task_xpath)
# 		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择HTTP类型
		self.browser_driver.click("xpath=>" + self.create_site_http_xpath)
# 		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.browser_driver
# 		self.find_element_by_link_text(u"创建监控项目").click()
# 		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[1]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("url").clear()
		self.find_element_by_id("url").send_keys(taskinfo["url"])
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_ping(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		if taskinfo.get('isagent') == 1:
			self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[5]").click()
			self.find_element_by_id("task_name").clear()
			self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
			self.find_element_by_id("host").clear()
			self.find_element_by_id("host").send_keys(taskinfo["host"])
			es = self.find_elements_by_css_selector("#agentOne>option")
			for e in es:
				#print e.get_attribute('value')
				if e.text.encode('utf-8') == taskinfo['agentname']: 
					e.click()
					agentSelect = True
			if 'agentSelect' not in vars(): raise ValueError("Agent %s does not exist on page!" %taskinfo['agentname'])
		else:
			self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[4]").click()
			self.find_element_by_id("task_name").clear()
			self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
			self.find_element_by_id("host").clear()
			self.find_element_by_id("host").send_keys(taskinfo["host"])
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_ftp(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[6]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("host").clear()
		self.find_element_by_id("host").send_keys(taskinfo["host"])
		self.find_element_by_id("ftp_port").clear()
		self.find_element_by_id("ftp_port").send_keys(taskinfo["ftp_port"])
		self.find_element_by_id("ftp_anonymous_%s" %taskinfo['ftp_anonymous']).click()
		time.sleep(3)
		if taskinfo['ftp_anonymous'] == 0:
			self.find_element_by_id("ftp_user").clear()
			self.find_element_by_id("ftp_user").send_keys(taskinfo['ftp_user'])
			self.find_element_by_id("ftp_pwd").clear()
			self.find_element_by_id("ftp_pwd").send_keys(taskinfo['ftp_pwd'])
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_dns(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择All Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[7]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("domain").clear()
		self.find_element_by_id("domain").send_keys(taskinfo["host"])
		self.find_element_by_css_selector("#__dns_type input[onclick*=%s]" %taskinfo["dns_type"]).click()
		time.sleep(2)
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_tcp(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择All Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		if taskinfo.get('isagent') == 1:
			self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[9]").click()
			self.find_element_by_id("task_name").clear()
			self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
			self.find_element_by_id("host").clear()
			self.find_element_by_id("host").send_keys(taskinfo["host"])
			self.find_element_by_id("tcp_port").clear()
			self.find_element_by_id("tcp_port").send_keys(taskinfo["tcp_port"])
			es = self.find_elements_by_css_selector("#agentOne>option")
			for e in es:
				#print e.get_attribute('value')
				if e.text.encode('utf-8') == taskinfo['agentname']:
					e.click()
					agentSelect = True
			if 'agentSelect' not in vars(): raise ValueError("Agent %s does not exist on page!" %taskinfo['agentname'])
		else:
			self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[8]").click()
			self.find_element_by_id("task_name").clear()
			self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
			self.find_element_by_id("host").clear()
			self.find_element_by_id("host").send_keys(taskinfo["host"])
			self.find_element_by_id("tcp_port").clear()
			self.find_element_by_id("tcp_port").send_keys(taskinfo["tcp_port"])
			time.sleep(2)
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_udp(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择All Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[10]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("host").clear()
		self.find_element_by_id("host").send_keys(taskinfo["host"])
		self.find_element_by_id("udp_port").clear()
		self.find_element_by_id("udp_port").send_keys(taskinfo["udp_port"])
		if taskinfo["req_format"] == 1:
			self.find_element_by_id("request_format_1").click()
		if taskinfo["req_format"] == 0:
			self.find_element_by_id("request_format_0").click()
		time.sleep(2)
		self.find_element_by_id("request_str").send_keys(taskinfo["req_str"])
		if taskinfo["pat_format"] == 1:
			self.find_element_by_id("pattern_format_1").click()
		if taskinfo["pat_format"] == 0:
			self.find_element_by_id("pattern_format_0").click()
		time.sleep(2)
		self.find_element_by_id("pattern_str").send_keys(taskinfo["pat_str"])
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_smtp(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择All Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[11]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("host").clear()
		self.find_element_by_id("host").send_keys(taskinfo["host"])
		self.find_element_by_id("smtp_port").clear()
		self.find_element_by_id("smtp_port").send_keys(taskinfo["smtp_port"])
		self.create_site_task_basic(taskinfo)
	
	
	def create_site_task_traceroute(self, taskinfo):
		#选择网站监控
		self.find_element_by_css_selector("div.header > div.header-nav > div:nth-of-type(2) a").click()
		time.sleep(3)
		#选择All Task类型
		self.find_element_by_css_selector("#sidebar .accordion-body > ul > li:nth-of-type(1) > a").click()
		time.sleep(3)
		self.find_element_by_link_text(u"创建监控项目").click()
		self.find_element_by_xpath(u"(//a[contains(text(),'创建项目')])[12]").click()
		self.find_element_by_id("task_name").clear()
		self.find_element_by_id("task_name").send_keys(taskinfo["taskname"])
		self.find_element_by_id("host").clear()
		self.find_element_by_id("host").send_keys(taskinfo["host"])
		if taskinfo["isagent"] == 1:
			self.find_element_by_id("use_agent").click()
			time.sleep(2)
			es = self.find_elements_by_css_selector("#agentOne>option")
			for e in es:
				#print e.get_attribute('value')
				if e.text.encode('utf-8') == taskinfo['agentname']:
					e.click()
					agentSelect = True
			if 'agentSelect' not in vars(): raise ValueError("Agent %s does not exist on page!" %taskinfo['agentname'])
		self.create_site_task_basic(taskinfo)
	
	
	def verify_site_task_info(self, taskinfo, tasktype):
		errmsg = "Expected element is not present!"
		self.print_site_task_info(taskinfo['taskname'], tasktype)
		try: host = taskinfo['url']
		except: host = taskinfo['host']
		#Verify the task basic info on task list page.
		#Temporoily disabled for verifying status picture and URL of task.
		#assert self.is_element_present("css selector", "#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(2)>img[src$='led_green.png']"), errmsg
		#assert self.is_element_present("css selector", "#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span[title=%s]" %taskinfo['url']), errmsg
		assert re.search(host, self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(5)>span").text), errmsg
		assert self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(6)>a").text == tasktype, errmsg
		assert re.search('分钟', self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(7) span").text.encode('utf-8')), errmsg
		#因为刚创建的任务在未触发监控频率前不会检查可用性，所以下面两项元素在刚创建任务时捕获不到。
		#assert re.search('%', self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(8) span").text.encode('utf-8')), errmsg
		#assert re.search('ms', self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(9) span").text.encode('utf-8')), errmsg
		print "Site task info verified correctly."
	
	
	def verify_site_task_detail(self, taskinfo, tasktype):
		errmsg = "Expected element is not present!"
		#Verify the task detail info on task list page.
		#Verify task overview.
		self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(4) a").click()
		time.sleep(5)
		self.driver.get_screenshot_as_file("/root/Desktop/overview.png")
		#print self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map #the_map #prov_time").text
		assert self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map #the_map #prov_time").text != 0
		#Verify task statistics of availability.
		self.find_element_by_css_selector(".site-monitor-main-body>.site-main-content>.site-monitor-left>ul>li:nth-of-type(2)>a").click()
		time.sleep(3)
		self.driver.get_screenshot_as_file("/root/Desktop/uptime.png")
		assert self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time")
		#print self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").rect
		#print self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").tag_name
		#self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").screenshot_as_png
		print "Site uptime: ", self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").text
		assert self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").text != 0
		#Verify task resptime_period
		self.find_element_by_css_selector(".site-monitor-main-body>.site-main-content>.site-monitor-left>ul>li:nth-of-type(3)>a").click()
		time.sleep(3)
		self.get_screenshot_as_file("/root/Desktop/resptime_period.png")
		assert self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time")
		print "Site resptime_period: ", self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").text
		assert self.find_element_by_css_selector(".site-monitor-main-body .site-monitor-right .site-map .border-bottom>#prov_time").text != 0
		#Verify site daily statistics. 
		self.find_element_by_css_selector(".site-monitor-main-body>.site-main-content>.site-monitor-left>ul>li:nth-of-type(4)>a").click()
		time.sleep(3)
		self.get_screenshot_as_file("/root/Desktop/daily_state.png")
		#Verify site snapshot.
		self.find_element_by_css_selector(".site-monitor-main-body>.site-main-content>.site-monitor-left>ul>li:nth-of-type(5)>a").click()
		time.sleep(3)
		self.get_screenshot_as_file("/root/Desktop/history_snapshot.png")
		print "Site task details verified correctly."
	
	
	def verify_site_task_detail_isagent(self, taskinfo, tasktype):
		errmsg = "Expected element is not present!"
		#Verify the task detail info on task list page.
		#Verify task overview.
		self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(4) a").click()
		time.sleep(5)
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(1)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/overview.png")
		#Verify task statistics of availability.
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(2)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/uptime.png")
		#Verify task resptime_period
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(3)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/resptime_period.png")
		#Verify task resptime
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(4)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/resptime.png")
		#Verify task google report
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(5)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/google_report.png")
		#Verify site daily statistics. 
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(6)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/daily_state.png")
		#Verify site history snapshot.
		self.find_element_by_css_selector("#main_body #nav .nav-body li:nth-of-type(7)>a").click()
		time.sleep(5)
		self.get_screenshot_as_file("/root/Desktop/history_snapshot.png")
	
	
	def delete_task(self, taskinfo, tasktype):
		if self.search_site_task(taskinfo, tasktype):
			#Delete the target task
			print "Deleting target task..."
			self.find_element_by_css_selector("#main .main_body #__task_list tbody>tr:nth-of-type(2)>td:nth-of-type(10) i.table_handle_icon.del").click()
			time.sleep(2)
			self.close_alert_and_get_its_text()
			print "Expected task deleted."
		else:
			msg = "No Expected Task Found!"
			raise NoSuchElementException(msg)
	
	
# 	
# 	def main():
# 		fp = webself.FirefoxProfile("/root/.mozilla/firefox/zig4k7m8.Default User")
# 		driver = webself.Firefox(fp)
# 		self.implicitly_wait(10)
# 		base_url = "http://qiye-qa.jiankongbao.com"
# 		verificationErrors = []
# 		accept_next_alert = True
# 		taskinfo = {'taskname':'Auto_Site_Task','url':'http://www.baidu.com','class':'classA','openscope':'用户组','frequency':7,'reminds':8,'retry':3,'history':1,'mongroup':'包含欧美监测点'}
# 	
	
