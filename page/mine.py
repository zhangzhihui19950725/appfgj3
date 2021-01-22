from common.base import BasePage
from page.bblist import Bblist
from page.mykh import Mykh
from page.sz import Sz


class Mine(BasePage):

    def click_mypic(self):
        self.click("id=>com.house365.xinfangbao:id/my_avatar")
        return self

    def click_mypicxc(self):
        self.click(("id=>com.house365.xinfangbao:id/more_service_layout"))



    def click_mysz(self):
        self.click("id=>com.house365.xinfangbao:id/iv_setting")
        return Sz(self.driver)

    def click_khnum(self):
        self.click("id=>com.house365.xinfangbao:id/tv_data_title_1")
        return Mykh(self.driver)

    def click_qynum(self):
        self.click("id=>com.house365.xinfangbao:id/tv_data_title_2")
        return Bblist(self.driver)

    def click_succesnum(self):
        self.click("id=>com.house365.xinfangbao:id/tv_data_title_3")
        return Bblist(self.driver)

    def click_myshop(self):
        self.click("text=>我的店铺")

    def click_mygz(self):
        self.click("text=>我的关注")

    def click_rz(self):
        self.click("text=>认证")


    def click_quan(self):
        self.click("text=>带看券")


    def click_dkjs(self):
        self.click("text=>贷款计算")

    def click_sfjs(self):
        self.click("text=>税费计算")

    def click_gfzg(self):
        self.click("text=>购房资格")

    def click_telbook(self):
        self.click("text=>通讯录")

    def click_tgb(self):
        self.click("text=>推广宝")

    def click_mdrz(self):
        self.swipe_to_buttom("门店入住")
        self.click("text=>门店入驻")

    def click_phz(self):
        self.swipe_to_buttom("项目合作")
        self.click("text=>项目合作")