#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage

class Sz(BasePage):

    def click_sz_grzl(self):
        self.click("text=>个人资料")

    def click_sz_edittel(self):
        self.click("text=>修改资料")

    def click_sz_editpwd(self):
        self.click("text=>修改密码")

    def click_sz_phsz(self):
        self.click("text=>偏好设置")

    def click_sz_qchz(self):
        self.click("text=>清理缓存")
        return self

    def click_sz_yj(self):
        self.click("text=>意见反馈")

    def click_sz_gy(self):
        self.click("text=>关于")

    def click_logout(self):
        self.click("text=>退出登录")
        self.click("text=>确定")
        from page.index import Index
        return Index(self.driver)





