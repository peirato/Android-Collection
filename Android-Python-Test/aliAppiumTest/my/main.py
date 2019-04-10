# -*- coding: utf-8 -*-
# MQC自动登陆

from appium import webdriver

# 引入desired_capabilities.py 配置文件
import desired_capabilities

# 使用python的unittest做单元测试
from unittest import TestCase
import unittest

import time


class MqcTest(TestCase):

    global automationName

    def setUp(self):
        # 获取capabilities， 通知Appium Server创建相应的会话
        desired_caps = desired_capabilities.get_desired_capabilities()

        # 获取server的地址
        uri = desired_capabilities.get_uri()

        # 获取使用的测试框架
        self.automationName = desired_caps.get('automationName')

        # 创建会话，得到driver对象
        self.driver = webdriver.Remote(uri, desired_caps)

    def test_searchbox(self):

        print("run test_searchbox - 测试开始")

        time.sleep(1)

        # 获取EditText控件
        edit_texts = self.driver.find_element_by_class_name("android.widget.EditText")

        print(edit_texts)

        # # == 0就是首次登陆提示页面
        # if len(edit_texts.size) == 0:
        #
        #     print("当前是首次登陆提示页面")

        # 向左滑动3次
        i = 0
        while i < 3:

            self.swipe_left()
            time.sleep(1)
            i = i + 1

        print("滑动结束")

        # 点击
        edit_texts.click()

        self.driver.find_element_by_id("com.emingren.xuebang:id/et_login_activity_username").send_keys('student3000')
        self.driver.find_element_by_id("com.emingren.xuebang:id/et_login_activity_password").send_keys('666888')
        self.driver.find_element_by_id("com.emingren.xuebang:id/btn_login_activity_login").click()

    def swipe_left(self):
        # width = self.manage().window().getSize().width
        # height = self.manage().window().getSize().height
        # width = self.driver.get_window_size('width')
        # height = self.driver.get_window_size('height')
        print(self.driver.get_window_size())
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print("width: "+str(width)+"height: "+str(height))
        self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, 300)
        print("向左滑动 from (width:"+str(width * 3 / 4)+",height:"+str(height / 2)+") to (width:"+str(width / 4)+",height:"+str(height / 2))

    def tearDown(self):
        # 测试结束，推出会话
        self.driver.quit()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
