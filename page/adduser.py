#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage


class Adduser(BasePage):
    def click_phone1(self):
        self.click("text=>通讯录导入")


    def send_name(self):
        self.find_element("text=>请输入客户姓名").send_keys("ceshi1")
        self.tsleep(1)
        return self

    def send_phone(self):
        self.find_element("text=>请输入客户手机号码").send_keys("17751300501")
        self.tsleep(1)
        return self

    def click_qy(self):
        self.find_element("text=>江宁区")
        self.tsleep(1)
        return self

    def slid_page(self):
        e1 = self.find_element("text=>大户型")
        self.swipe_to_buttom(e1)


