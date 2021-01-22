#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
import os


class Search(BasePage):

    def search_lp(self,value):
        self.send_text("id=>com.house365.xinfangbao:id/edit_search_query",value)
        return self

    def adbshell(self,command):
        os.system(command)

    def action_seach(self):
        self.adbshell('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')
        self.tsleep(3)
        self.click("id=>com.house365.xinfangbao:id/edit_search_query")
        self.driver.press_keycode('66')  # os.system("adb shell input keyevent 66"),66:回车，84:搜索
        self.tsleep(3)
        self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        self.tsleep(3)
        return self





