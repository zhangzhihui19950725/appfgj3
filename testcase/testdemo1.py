#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time

from appium import webdriver
import pytest

class Testdemo():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "7"
        caps["deviceName"] = "2e72982d"
        caps["appPackage"] = "com.house365.xinfangbao"
        caps["appActivity"] = "com.house365.xinfangbao.ui.activity.SplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait("10")


    def teardown(self):
        self.driver.quit()

    def waitActivity(self, page_name, seconds):
        self.driver.wait_activity(page_name, seconds)
        print("-----wait  %s  ----" %page_name)

    def test_login(self):
        self.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("客户")').click()
        print("------")
        self.driver.find_element_by_id('com.house365.xinfangbao:id/ed_ss_phone').send_keys('13813996588')
        print("开始输入密码")
        self.driver.find_element_by_id('com.house365.xinfangbao:id/ed_ss_pwd').send_keys('123456qwe')
        print("开始点击登录")
        e2 = self.driver.find_element_by_id('com.house365.xinfangbao:id/bt_ss_commit')
        time.sleep(1)
        e2.click()