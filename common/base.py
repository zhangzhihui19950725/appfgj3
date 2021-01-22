#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @FileName    :base_methods.py
# @Description :将appium中的部分函数进行封装

import os
import time

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from common.get_deviceinfo import get_device_info


class BasePage:
    """
    将appium中的内容封装到该类下，供上一级使用
     Attributes:
    """
    def __init__(self,driver: WebDriver=None):
        """
        此类的构造函数，将driver传入

        """
        self.driver = driver
        self.foldpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screen//'



    def find_element(self, selector):
        """
        查找元素
        Args：
            selector:
            1、id=>abd，通过id来查找一个元素
            2、text=>淘房，通过text来查找一个元素
            3、elements=>id=>abd=>0，通过id来查找一组元素，并返回pos位置的元素，目前仅支持id查找
            4、abd，直接通过id来查找
            5、xpath=>abd，通过xpath来查找一个元素
        Returns：
            element：查找到的元素
        """
        print("find_element: ", selector)
        if "=>" not in selector:
            return self.driver.find_element_by_id(selector)

        if self.driver is None:
            print("+++++++++")

        if "elements" in selector:
            type = selector.split('=>')[1]
            value = selector.split('=>')[2]
            pos = selector.split('=>')[3]

            try:
                elements = self.driver.find_elements_by_id(value)
            except NoSuchElementException as e:
                print("No Such Element Exception: %s" % e)

            return elements[int(pos)]

        type = selector.split('=>')[0]
        value = selector.split('=>')[1]

        if type == "id":
            try:
                element = self.driver.find_element_by_id(value)
            except NoSuchElementException as e:
                print("%s cant click: %s" % (selector, e))
        if type == "text":
            try:
                element = self.driver.find_element_by_android_uiautomator('new UiSelector().text(\"' + value + '\")')
            except NoSuchElementException as e:
               print("%s cant click: %s" % (selector, e))

        if type == "xpath":
            try:
                element = self.driver.find_element_by_xpath(value)
            except NoSuchElementException as e:
                print("%s cant click: %s" % (selector, e))

        return element

    def click(self, selector):
        """
        点击元素
        """
        el = self.find_element(selector)
        print("click: ", el)
        try:
            self.tsleep()
            el.click()
            self.tsleep()
        except NoSuchElementException as e:
            print("%s cant click: %s" % selector % e)

    def send_text(self, selector, text):
        """
        输入文本框内容
        """
        el = self.find_element(selector)
        el.clear()
        try:
            self.tsleep(1)
            el.send_keys(text)
        except NoSuchElementException as e:
            print("%s cant send keys %s:%s" % selector % text % e)

    def is_in_pagesource(self, selector):
        """
        判断selector是否在页面中
        1、在的话，返回True
        2、不在的话，返回False
        """
        if selector in self.driver.page_source:
            return True
        else:
            return False

    def wait(self, page_name=None, seconds=10):
        """
        等待，包括2个：
        1、等待页面加载，超时默认为10s
        2、等待查找到元素page_name=None，超时默认为10s
        """
        print("wait le ma ~")
        if (page_name == None):
            self.driver.implicitly_wait(seconds)
        else:
            self.driver.wait_activity(page_name, seconds)

    def tsleep(self, sec=3):
        """
        休息时长，默认为3s
        """
        time.sleep(3)

    def swipe_to_buttom(self, text=None):
        """
        text=None:	直接滑动到页面底部
        text!=None:	滑动到text的地方
        """
        device_size = self.driver.get_window_size()
        p_e = self.driver.page_source

        while (1):
            p_s = p_e
            if text != None and (text in p_s):
                break
            s_x = device_size['width'] * 0.5
            s_y = device_size['height'] * 0.75
            e_y = device_size['height'] * 0.5
            self.driver.swipe(s_x, s_y, s_x, e_y, 500)
            p_e = self.driver.page_source
            time.sleep(1)
            if p_s == p_e:
                print("找到所需要的地方！退出")
                break

    def get_current_activity(self):
        """
        返回当前页面activity
        """
        return self.driver.current_activity

    def save_screenshot_as_file(self, filename):
        """
        保存当前页面的截图到项目文件夹下的screen文件夹下
        """
        self.tsleep(3)
        #foldpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screen//'
        filepath = self.foldpath + filename + '.png'
        self.driver.get_screenshot_as_file(filepath)
        self.tsleep(3)

    def waitActivity(self, page_name, seconds):
        """
        等待页面activity
        """
        self.driver.wait_activity(page_name, seconds)


    def quit(self):
        self.driver.quit()

