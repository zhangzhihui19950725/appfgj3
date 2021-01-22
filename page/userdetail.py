#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
from page.edituser import Edituser


class Userdetail(BasePage):

    def click_uesredit(self):
        self.click("text=>编辑")
        return Edituser(self.driver)

    def click_phone(self):
        self.click("id=>com.house365.xinfangbao:id/customer_detail_call_img")



