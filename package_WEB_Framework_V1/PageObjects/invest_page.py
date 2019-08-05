#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: july
# Time: 2019/7/31

from selenium.webdriver.common.by import By

from package_WEB_Framework_V1.PageObjects.mix_page import MixInPage


class InvestPage(MixInPage):
    # 用户初始余额显示框
    balance_loc = (By.XPATH, '//div[@class="clearfix left"]/input')
    # 第一个抢投标按钮
    first_button = (By.XPATH, '//div[@class="b-unit-list clearfix"]/div[1]//a[contains(text(), "抢投标")]')
    # 输入完后，点击投标按钮
    confirm_button = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 查看并激活按钮
    active_loc = (By.XPATH, '//div[@class="layui-layer-content"]//button[contains(text(), "查看并激活")]')
    # 可用余额
    remain_loc = (By.XPATH, '//li[@class="color_sub"]')

    def click_invest(self):
        self.wait_widget(self.first_button)
        self.get_widget(self.first_button).click()

    def get_init_balance(self):
        self.wait_widget(self.balance_loc)
        return self.get_widget(self.balance_loc).get_attribute("data-amount")

    def input_invest_amount(self, amount):
        self.wait_widget(self.balance_loc)
        self.get_widget(self.balance_loc).send_keys(amount)
        self.get_widget(self.confirm_button).click()
        self.wait_widget(self.active_loc)
        self.get_widget(self.active_loc).click()

    def get_aft_balance(self):
        self.wait_widget(self.remain_loc)
        return self.get_widget(self.remain_loc).text[:-1]
