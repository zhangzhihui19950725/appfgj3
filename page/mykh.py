#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
from page.adduser import Adduser
from page.uesrsearch import Usersearch
from page.userdetail import Userdetail


class Mykh(BasePage):


    def click_add(self):
        self.click("id=>com.house365.xinfangbao:id/tv_nav_right")
        return Adduser(self.driver)
        pass

    def click_search(self):
        self.click('xpath=>//*[@class="android.widget.ImageView"][1]')
        return Usersearch(self.driver)

    def goto_userdetail(self):
        """
        点击第一个客户
        :return:
        """
        self.click('xpath=>//*[@resource-id="com.house365.xinfangbao:id/customer_list_name_tx"][1]')
        return Userdetail(self.driver)

