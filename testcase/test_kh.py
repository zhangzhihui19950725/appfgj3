#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time

from appium import webdriver
import pytest

from common.app import App
from common.base import BasePage
from common.get_deviceinfo import get_device_info
from page.index import Index


class Testkh():
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.quit()

    def test_kh(self):
        """
        首页，点击客户，进入客户页面
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().goto_kh()
        assert self.app.find_element("text=>我的客户")
        self.app.save_screenshot_as_file("test_kh")


    def test_kh_clickwdbb(self):
        """
        已登录，客户->点击我的客户
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh()
        assert self.app.find_element("text=>我的客户")
        self.app.save_screenshot_as_file("test_kh_clickwdbb")


    def test_kh_mybb(self):
        """
        已登录，客户->点击我的报备
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_wdbb()
        assert self.app.find_element("text=>报备列表")
        self.app.save_screenshot_as_file("test_kh_mybb")



    def test_kh_clickaddkh(self):
        """
        已登录，客户->点击添加客户
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_addkh()
        assert self.app.find_element("text=>添加客户")
        self.app.save_screenshot_as_file("test_kh_clickaddkh")


    def test_kh_clickqbb(self):
        """
        已登录，点击客户->点击快速报备
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_qbb()
        assert self.app.find_element("text=>报备客户")
        self.app.save_screenshot_as_file("test_kh_clickqbb")

    def test_kh_search(self):
        """
        已登录，客户->点击搜索
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_search()
        assert self.app.find_element("text=>请输入客户姓名、手机号码")
        self.app.save_screenshot_as_file("test_kh_search")


    def test_kh_sx(self):
        """
         已登录，客户->点击筛选
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_khsx()

    def test_kh_sx1(self):
        """
        已登录，客户—>筛选，点击‘已签约’
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_khsx().click_state1()

    def test_kh_mykh_add(self):
        """
        已登录，客户—>我的客户->点击“+’
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh().click_add()


    def test_kh_mykh_search(self):
        """
        已登录，客户—>我的客户->点击“搜索’
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh().click_search()


    def test_kh_mykh_clickkh(self):
        """
        已登录，客户—>我的客户->点击客户
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh().goto_userdetail()


    def test_kh_mykh_detailedit(self):
        """
        已登录，客户->我的客户，客户详情页->编辑
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh().goto_userdetail().click_uesredit()

    def test_kh_mykh_detailtel(self):
        """
        客户->我的客户，客户详情页->点击电话
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_mykh().goto_userdetail().click_phone()

    def test_kh_addkh_tel(self):
        """
        已登录，点击客户->点击添加客户,点击通讯录导入
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_addkh().click_phone1()

    def test_kh_addkh_edit1(self):
        """
        已登录，点击客户->点击添加客户,输入手机号和姓名
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_addkh().send_name().send_phone()

    def test_kh_addkh_edit2(self):
        """
        已登录，点击客户->点击添加客户,点击“江宁区”
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_addkh().click_qy()

    def test_kh_addkh_edit3(self):
        """
        已登录，点击客户->点击添加客户,滑动到底部
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_addkh().slid_page()

    def test_kh_quickbb1(self):
        """
        已登录，点击客户->点击快速报备，点击“从客户列表添加”
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_qbb().click_ueselistadd()

    def test_kh_quickbb1(self):
        """
        已登录，点击客户->点击快速报备，点击“请选择楼盘”
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_kh().goto_qbb().click_lp()

    def test_msg_clickmsg1(self):
        """
        已登录，点击消息->点击客户提醒
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_msg().click_khmsg()

    def test_msg_clickmsg2(self):
        """
        已登录，点击消息->点击系统消息
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_msg().click_xtmsg()

    def test_msg_clickmsg3(self):
        """
        点击消息->点击楼盘动态
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_msg().click_lpmsg()































if __name__ == "__main__":
    pytest.main()