#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
from page.mykh import Mykh


class Bbkh(BasePage):

    def click_ueselistadd(self):
        self.click("text=>从客户列表添加")
        return Mykh(self.driver)

    def click_lp(self):
        self.click("text=>请选择楼盘")



