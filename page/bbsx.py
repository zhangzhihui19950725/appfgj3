#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.base import BasePage


class Bbsx(BasePage):

    def click_state1(self):
        """
        选中“已签约”
        :return:
        """
        self.click("text=>已签约")
        return self
