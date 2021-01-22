#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.app import App


class TestIndex:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.quit()


    def test_open_index(self):
        """
        打开首页
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index()
        assert self.app.find_element("text=>首页")
        self.app.save_screenshot_as_file("test_open_index")

    def test_search(self):
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_index_search().search_lp("万")
        self.app.tsleep(1)

    def test_search2(self):
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_index_search().search_lp("万").action_seach()



    def test_click_all(self):
        """
        首页=》功能入口=》全部
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_all()
        assert self.app.find_element("text=>请输入楼盘名称")
        self.app.save_screenshot_as_file("test_click_all")

    def test_click_zz(self):
        """
        首页=》功能入口=》住宅
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zz()
        assert self.app.find_element("text=>请输入楼盘名称")
        self.app.save_screenshot_as_file("test_click_zz")

    def test_click_shy(self):
        """
        首页=》功能入口=》商业
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_shy()
        assert self.app.find_element("text=>请输入楼盘名称")
        self.app.save_screenshot_as_file("test_click_shy")

    def test_click_gy(self):
        """
        首页=》功能入口=》公寓
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_gy()
        assert self.app.find_element("text=>请输入楼盘名称")
        self.app.save_screenshot_as_file("test_click_gy")

    def test_click_sz_logged(self):
        """
        点击首页->我的->若未登录则登录->智能推荐->设置
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().swap_zntj().click_sz()
        assert self.app.find_element("text=>偏好设置")
        self.app.save_screenshot_as_file("test_click_sz_logged")

    def test_click_znyj_lp(self):
        """
        点击首页->智能推荐->楼盘
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zh().swap_zntj().click_znfirstlp()
        assert self.app.find_element("text=>楼盘详情")
        self.app.save_screenshot_as_file("test_click_znyj_lp")



    def test_click_zxpx(self):
        """
        点击首页->精选推荐->综合排序
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zh()
        assert self.app.find_element("text=>综合排序")
        self.app.save_screenshot_as_file("test_click_zhpv")


    def test_click_zxsj(self):
        """
        点击首页->精选推荐->最新上架
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zx()
        assert self.app.find_element("text=>最新上架")
        self.app.save_screenshot_as_file("test_click_zxsj")

    def test_click_rmbb(self):
        """
        点击首页->精选推荐->热门报备
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_rm()
        assert self.app.find_element("text=>热门报备")
        self.app.save_screenshot_as_file("test_click_rmbb")

    def test_click_zh_lp(self):
        """
        点击首页->精选推荐->综合排序->楼盘
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zh().swap_jxtj().click_jxfirstlp()
        assert self.app.find_element("text=>楼盘详情")
        self.app.save_screenshot_as_file("test_click_zh_lp")

    def test_click_zx_lp(self):
        """
        点击首页->精选推荐->最新上架->楼盘
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zh().swap_jxtj().click_zx().click_jxfirstlp()
        assert self.app.find_element("text=>楼盘详情")
        self.app.save_screenshot_as_file("test_click_zx_lp")

    def test_click_rm_lp(self):
        """
        点击首页->精选推荐->热门报备->楼盘
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 60)
        self.app.index().click_zh().swap_jxtj().click_rm().click_jxfirstlp()
        assert self.app.find_element("text=>楼盘详情")
        self.app.save_screenshot_as_file("test_click_rm_lp")





















