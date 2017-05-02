# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：定义Pyse类，封装了selenium提供的页面元素操作方法，用于所有页面的继承
'''
import sys,os,time
if ".." not in sys.path:
    sys.path.append("../packages")
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tools import getConfigData
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class Pyse(object):
    @classmethod
    def __init__(self, browser,env):
        self.env = env
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        self.browser = browser
        if browser == "firefox" or browser == "ff":
#             远程运行用例
            host ='127.0.0.1:4444'
#             dc = {'browserName':'firefox'}
#             dirver = Remote(command_executor = 'http://'+host+'/wd/hub',desired_capabilities = dc)
#             dirver = Remote(command_executor = 'http://'+host+'/wd/hub',desired_capabilities = DesiredCapabilities.FIREFOX)
            dirver = Remote(command_executor = 'http://'+host+'/wd/hub',desired_capabilities={'platform':'ANY','browserName':'firefox','version': '','javascriptEnabled':True})      
#             本地firefox配置
#             driver = webdriver.Firefox()
#             profile = webdriver.FirefoxProfile()
#             profile.set_preference("browser.startup.homepage", "about:blank")
#             profile.set_preference("startup.homepage_welcome_url", "about:blank")
#             profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
#             profile = webdriver.FirefoxProfile()
#             profile.assume_untrusted_cert_issuer =True
#             accept_untrusted_certs = True
#             driver = webdriver.Firefox(profile)
        elif browser == "chrome":
            driver = webdriver.Chrome('../packages')
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)
#     
    def open_url(self,url):
        self.driver.get(url)
        
    def open_homPage(self):
        '''根据环境获取主页url'''
        env_dict = getConfigData.get_config(self.env)
        self.home_url = env_dict['homepage_url']
        self.driver.get(self.home_url)
#     def open_homPage(self):
#         '''根据环境获取主页url'''
#         env_dict = getConfigData.get_config(self.env)
#         self.home_url = env_dict['homepage_url']
#         self.driver.get(self.home_url)        
    def script(self,src):
        return self.driver.execute_script(src)
    
    def find_element(self,xpath):
        try:
            return self.driver.find_element(By.XPATH(xpath))
        except Exception as reason:
            print '找不到元素' + str(reason)
            
    def element_wait(self, css, secs=5):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,secs,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def get_element(self,css):
        '''
        Judge element positioning way, and returns the element.
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]
        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        return element

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)
    def insert_img(self,file_name):
    #         项目路径
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#         sys.path.append(proDir)
        JBKDir =  os.path.join(proDir, "JKB")
#         sys.path.append(JBKDir)
#         report目录路径

        reportPath = os.path.join(JBKDir, "report")
#         screenPath = os.path.join(reportPath, "image")
        screenPath = os.path.join(reportPath,"image" + os.path.sep)
#         '''获取上级目录'''
#         base_dir =str(os.path.dirname(os.path.dirname(__file__)))
#         '''截图保存'''
#         screen_path = base_dir + "/JKB/report/image/"
#         print screen_path
        self.driver.get_screenshot_as_file(screenPath + "%s.png" %(file_name + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))))
if __name__ == '__main__':
    pass
#     d= Pyse("ff",'jkb_qa')
#     d.insert_img("aa")
#     print d.f
#     d.open_homPage()
#     d.clear("id=>kw")
#     d.type("id=>kw", "pyse")
#     d.click("css=>#su")
#     d.wait(10)
#     d.quit()
