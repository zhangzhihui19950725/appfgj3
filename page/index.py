#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage
from page.detail import Hdetail
from page.kh import Kh
from page.list import List
from page.login import Login
from page.mine import Mine
from page.msg import Msg
from page.search import Search


class Index(BasePage):



    def goto_index(self):
        self.click("text=>首页")

    def goto_kh(self):
        self.click("text=>客户")

        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()

            return Kh(self.driver)
        else:
            return Kh(self.driver)

    def goto_msg(self):
        """
        如果未登录，先登录，再跳转至消息页面
        如果已登录，直接跳转至消息页面
        :return:
        """
        self.click("text=>消息")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            return Msg(self.driver)
        else:
            return Msg(self.driver)


    def goto_mine(self):
        """
        未登录，先登录，再跳转我的页面
        如果已登录，直接跳转至消我的页面
        :return:
        """
        self.click("text=>我的")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            return Mine(self.driver)
        else:
            return Mine(self.driver)

    def click_index_search(self):
        self.click("id=>com.house365.xinfangbao:id/tv_index_search")
        return Search(self.driver)


    def click_all(self):
        self.click("text=>全部")
        return List(self.driver)

    def click_zz(self):
        self.click("text=>住宅")
        return List(self.driver)

    def click_shy(self):
        self.click("text=>商业")
        return List(self.driver)

    def click_gy(self):
        self.click("text=>公寓")
        return List(self.driver)


    def click_sz(self):
        self.click("id=>com.house365.xinfangbao:id/tv_index_recommend_setting")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            if self.find_element("text=确定"):
                self.click("text=确定")


    def click_zh(self):
        self.swipe_to_buttom("综合排序")
        self.click("text=>综合排序")
        return self

    def click_zx(self):
        self.swipe_to_buttom("最新上架")
        self.click("text=>最新上架")
        return self

    def click_rm(self):
        self.swipe_to_buttom("热门报备")
        self.click("text=>热门报备")
        return self

    def swap_zntj(self):
        self.swipe_to_buttom("智能推荐")
        return self

    def swap_jxtj(self):
        self.swipe_to_buttom("精选推荐")
        return self

    def click_znfirstlp(self):
        self.click("elements=>id=>com.house365.xinfangbao:id/iv_house_recommend_image=>0")
        #ele = self.find_element("xpath=>//*[@resource-id='com.house365.xinfangbao:id/iv_house_recommend_image]'[1]")
        #self.click(ele)
        return Hdetail(self.driver)


    def click_jxfirstlp(self):
        self.click("elements=>id=>com.house365.xinfangbao:id/iv_image=>0")
        return Hdetail(self.driver)
















