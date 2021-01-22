#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage


class Login(BasePage):

    def login(self):
        print("开始输入手机")
        phone = self.find_element('id=>com.house365.xinfangbao:id/ed_ss_phone')
        self.tsleep(1)
        phone.send_keys('15100000002')
        print("开始输入密码")
        pwd = self.find_element('id=>com.house365.xinfangbao:id/ed_ss_pwd')
        self.tsleep(1)
        pwd.send_keys('123456qwe')
        print("开始点击登录")
        self.click('id=>com.house365.xinfangbao:id/bt_ss_commit')









