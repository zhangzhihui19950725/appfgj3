#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage


class Msg(BasePage):

    def click_khmsg(self):
        self.click("text=>客户提醒")


    def click_xtmsg(self):
        self.click("text=>系统消息")


    def click_lpmsg(self):
        self.click("text=>楼盘动态")

