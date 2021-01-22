#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver

from common.base import BasePage
from common.get_deviceinfo import get_device_info
from page.index import Index


class App(BasePage):
    def start(self):


        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "7"
        #caps["deviceName"] = "OB6585TSDYUGNJSC"
        caps["deviceName"]="2e72982d"
        caps['unicodeKeyboard'] = "true"
        caps["appPackage"] = "com.house365.xinfangbao"
        caps["appActivity"] = "com.house365.xinfangbao.ui.activity.SplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait("10")


        #self.url, self.desired_caps = get_device_info('D:\\appium\\appfgj3\common\device_info_file.txt')
        # print(self.desired_caps)
        #self.driver = webdriver.Remote(self.url, self.desired_caps)

        return self


    def stop(self):
        self.driver.quit()

    def index(self) -> Index:
        return Index(self.driver)