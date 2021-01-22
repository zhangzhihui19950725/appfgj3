#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from common.app import App


class Testmy:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.quit()


    def test_mine(self):
        """
        点击我的
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine()
        assert self.app.find_element("text=>客户数")
        self.app.save_screenshot_as_file("test_mine")


    def test_click_mypic(self):
        """
        进入我的页面，点击头像
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mypic()
        self.app.save_screenshot_as_file("test_click_mypic")

    def test_click_mupic_xc(self):
        """
        进入我的页面，点击头像
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mypic().click_mypicxc()
        assert self.app.find_element("text=>图片")
        self.app.save_screenshot_as_file("test_click_mypic_xc")


    def test_click_mysz(self):
        """
        我的-设置
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz()
        assert self.app.find_element("text=>设置")
        self.app.save_screenshot_as_file("test_click_mysz")

    def test_click_khnum(self):
        """
        我的-客户数
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_khnum()
        assert self.app.find_element("text=>我的客户")
        self.app.save_screenshot_as_file("test_click_khnum")

    def test_click_qynum(self):
        """
        我的-签约量
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_qynum()
        assert self.app.find_element("text=>报备列表")
        self.app.save_screenshot_as_file("test_click_qynum")


    def test_click_successnum(self):
        """
        我的-成交额
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_succesnum()
        assert self.app.find_element("text=>报备列表")
        self.app.save_screenshot_as_file("test_click_successnum")

    def test_click_myshop(self):
        """
        我的-我的店铺
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_myshop()
        assert self.app.find_element("text=>推广我的店铺")
        self.app.save_screenshot_as_file("test_click_myshop")

    def test_click_mygz(self):
        """
        我的-我的关注
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mygz()
        assert self.app.find_element("text=>收藏")
        self.app.save_screenshot_as_file("test_click_mugz")

    def test_click_rz(self):
        """
        我的-认证
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_rz()
        assert self.app.find_element("text=>认证")
        self.app.save_screenshot_as_file("test_click_rz")

    def test_click_dkquan(self):
        """
        我的-带看券
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_quan()
        assert self.app.find_element("text=>奖券")
        self.app.save_screenshot_as_file("test_click_dkquan")

    def test_click_dkjs(self):
        """
        我的-贷款计算
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_dkjs()
        assert self.app.find_element("text=>贷款计算")
        self.app.save_screenshot_as_file("test_click_dkjs")

    def test_click_sfjs(self):
        """
        我的-税费计算
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_sfjs()
        assert self.app.find_element("text=>税费计算")
        self.app.save_screenshot_as_file("test_click_sfjs")


    def test_click_gfzg(self):
        """
        我的-购房资格
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_gfzg()
        self.app.save_screenshot_as_file("test_click_gfzg")

    def test_click_txl(self):
        """
         我的-通讯录
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_telbook()
        self.app.save_screenshot_as_file("test_click_txl")

    def test_click_tgb(self):
        """
        我的-推广宝
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_tgb()
        assert self.app.find_element("text=>推广宝")
        self.app.save_screenshot_as_file("test_click_tgb")

    def test_click_mdrz(self):
        """
        我的-门店入驻
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mdrz()
        assert self.app.find_element("text=>门店入驻")
        self.app.save_screenshot_as_file("test_click_mdrz")

    def test_click_phz(self):
        """
        我的-项目合作
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_phz()
        assert self.app.find_element("text=>合作留言")
        self.app.save_screenshot_as_file("test_click_phz")

    def test_click_sz_grzl(self):
        """
        我的－设置－个人资料
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_grzl()
        assert self.app.find_element("text=>个人资料")
        self.app.save_screenshot_as_file("test_click_sz_grzl")

    def test_click_sz_edittel(self):
        """
        我的-设置-修改手机
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_edittel()
        assert self.app.find_element("text=>修改手机")
        self.app.save_screenshot_as_file("test_click_sz_edittel")

    def test_click_sz_editpwd(self):
        """
        我的-设置-修改密码
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_editpwd()
        assert self.app.find_element("text=>修改密码")
        self.app.save_screenshot_as_file("test_click_sz_editpwd")

    def test_click_sz_phsz(self):
        """
        我的-设置-偏好设置
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_phsz()
        assert self.app.find_element("text=>偏好设置")
        self.app.save_screenshot_as_file("test_click_sz_phsz")

    def test_click_qchc(self):
        """
        我的-设置-清理缓存
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_qchz()
        self.app.save_screenshot_as_file("test_click_sz_qchc")

    def test_click_sz_yjfk(self):
        """
        我的-设置-意见反馈
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_yj()
        assert self.app.find_element("text=>意见反馈")
        self.app.save_screenshot_as_file("test_click_sz_yjgk")


    def test_click_sz_gy(self):
        """
        我的-设置-关于
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_sz_gy()
        assert self.app.find_element("text=>关于")
        self.app.save_screenshot_as_file("test_click_sz_gy")

    def test_click_sz_logout(self):
        """
        我的-设置-退出
        :return:
        """
        self.app.waitActivity(".ui.activity.index.IndexActivity", 50)
        self.app.index().goto_mine().click_mysz().click_logout()
        assert self.app.find_element("text=>全部")
        self.app.save_screenshot_as_file("test_click_sz_logout")






















