#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
from page.adduser import Adduser
from page.bbkh import Bbkh
from page.bbsx import Bbsx
from page.mdbb import Bblist
from page.mykh import Mykh
from page.uesrsearch import Usersearch


class Kh(BasePage):

    def goto_mykh(self):
        self.click("text=>我的客户")
        return Mykh(self.driver)

    def goto_wdbb(self):
        self.click("text=>我的报备")
        return Bblist(self.driver)

    def goto_addkh(self):
        self.click("text=>添加客户")
        return Adduser(self.driver)

    def goto_qbb(self):
        self.click("text=>快速报备")
        return Bbkh(self.driver)

    def goto_search(self):
        self.click("id=>com.house365.xinfangbao:id/ib_customers_search")
        return Usersearch(self.driver)

    def goto_khsx(self):
        self.click("id=>com.house365.xinfangbao:id/ib_customers_choice")
        return Bbsx(self.driver)






