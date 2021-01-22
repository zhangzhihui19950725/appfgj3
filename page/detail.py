from common.base import BasePage
from page.login import Login


class Hdetail(BasePage):

    def click_xc(self):  #点击相册
        self.click("id=>com.house365.xinfangbao:id/tv_housedetail_imagecount")

    def click_share(self):
        self.click("id=>com.house365.xinfangbao:id/ib_nav_right")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            return self
        else:
            return self

    def click_pfa(self):
        self.click("text=>项目方案")
        return self

    def click_pdt(self):
        self.click("text=>项目动态")
        return self

    def click_pdetail(self):
        self.click("text=>项目详情")
        return self


    def click_moredetail(self):
        self.click("id=>com.house365.xinfangbao:id/tv_housedetail_projectinfo_more")

    def swap_moredetail(self):
        self.swipe_to_buttom("更多项目信息")
        return self

    def swap_detaildb(self):
        if self.find_element("text=>合作动态"):
            self.swipe_to_buttom("合作动态")
        else:
            self.swipe_to_buttom("已报备客户")



    def click_sc(self):
        self.click("id=>com.house365.xinfangbao:id/iv_housedetail_collect")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            self.click("id=>com.house365.xinfangbao:id/iv_housedetail_collect")
            return self
        else:
            return self

    def click_hb(self):
        self.click("text=>海报")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()


    def click_gt(self):
        self.click("id=>com.house365.xinfangbao:id/tv_detail_tel")


    def click_bb(self):
        self.click("id=>com.house365.xinfangbao:id/tv_detail_baobei")
        if self.driver.current_activity == '.ui.activity.sign.SignInActivity':
            Login(self.driver).login()
            self.click("id=>com.house365.xinfangbao:id/tv_detail_baobei")
        if self.find_element("text=>确定"):
            self.click("text=>确定")
