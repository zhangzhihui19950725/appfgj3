#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.app import App


class TestDetail:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.quit()

    def test_click_xc(self):
        """
        进入楼盘详情页，点击楼盘相册
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_xc()
        self.app.find_element("text=>楼盘相册")
        self.app.save_screenshot_as_file("test_click_xc")

    def test_click_share(self):
        """
        进入楼盘详情页，点击分享
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_share()
        self.app.save_screenshot_as_file("test_click_share")

    def test_click_pfa(self):
        """
        进入楼盘详情页，点击项目方案
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_pfa()
        self.app.save_screenshot_as_file("test_click_pfa")

    def test_click_pdetail(self):
        """
            进入楼盘详情页，点击项目详情
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_pdetail()
        self.app.save_screenshot_as_file("test_click_pdetail")


    def test_click_pdetail2(self):
        """
        楼盘详情页-切换至项目详情，点击更多项目信息
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_pdetail().swap_moredetail().click_moredetail()
        assert self.app.find_element("text=>项目信息")
        self.app.save_screenshot_as_file("test_click_pdetail2")


    def test_click_sc(self):
        """
        楼盘详情页，点击关注，若未登录，则登录
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_sc()
        self.app.save_screenshot_as_file("test_click_sc")

    def test_click_hb(self):
        """
        楼盘详情页，点击海报，若未登录，则登录
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_hb()
        self.app.save_screenshot_as_file("test_click_hb")


    def test_click_gt(self):
        """
        楼盘详情页，点击沟通
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_gt()
        self.app.save_screenshot_as_file("test_click_gt")


    def test_click_lp_bb(self):
        """
        楼盘详情页，点击报备，若未登录，则登录
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().swap_zntj().click_znfirstlp().click_bb()
        self.app.save_screenshot_as_file("test_click_p_bb")















