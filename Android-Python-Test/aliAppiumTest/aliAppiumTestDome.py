# MQC测试脚本dome  http://mqc.aliyun.com/doc.htm?id=17

# -*- coding: utf-8 -*-

from appium import webdriver

# 引入刚刚创建的同目录下的desired_capabilities.py
import desired_capabilities

# 我们使用python的unittest作为单元测试工具
from unittest import TestCase

# 我们使用python的unittest作为单元测试工具
import unittest

# 使用time.sleep(xx)函数进行等待
import time


class MqcTest(TestCase):
    global automationName

    def setUp(self):
        # 获取我们设定的capabilities，通知Appium Server创建相应的会话。
        desired_caps = desired_capabilities.get_desired_capabilities()
        # 获取server的地址。
        uri = desired_capabilities.get_uri()
        # 获取使用的测试框架
        self.automationName = desired_caps.get('automationName')
        # 创建会话，得到driver对象，driver对象封装了所有的设备操作。下面会具体讲。
        self.driver = webdriver.Remote(uri, desired_caps)

    def test_searchbox(self):
        # 找到包含”Tab4”字符串的控件。
        if self.automationName == 'Appium':
            tab4 = self.driver.find_element_by_name("Tab4")
        else:
            tab4 = self.driver.find_element_by_link_text("Tab4")
        # 点击.
        tab4.click()
        # 打印步骤描述 并 截图
        print("STEP : %s" % ("点击包含'Tab4'字符串的控件"))
        print("SCREENSHOT : %s" % "0")

        # 等待2秒钟
        time.sleep(2)
        print("STEP : %s" % ("等待 2s"))
        print("SCREENSHOT : %s" % "1")

        # 通过控件类名找到用户名和密码输入框。
        editTexts = self.driver.find_elements_by_class_name("android.widget.EditText")
        # 第一个框为用户名输入框，输入用户名；第二个框为密码框，输入密码
        editTexts[0].send_keys("admin")
        print("STEP : %s" % ("输入用户名 admin"))
        print("SCREENSHOT : %s" % "2")

        editTexts[1].send_keys("admin")
        print("STEP : %s" % ("输入密码 admin"))
        print("SCREENSHOT : %s" % "3")

        # 隐藏出现的软键盘
        self.driver.hide_keyboard()
        print("STEP : %s" % ("隐藏出现的软键盘"))
        print("SCREENSHOT : %s" % "3")
        # 步骤执行失败，打印日志 FATAL : xxx
        print("FATAL : %s" % (执行失败))

        # 找到包含“登录”的按钮并点击
        if self.automationName == 'Appium':
            self.driver.find_element_by_name("登陆").click()
        else:
            self.driver.find_element_by_link_text("登陆").click()
        # 等待3秒钟，登录需要与服务器通讯。
        time.sleep(3)

    def tearDown(self):
        # 测试结束，退出会话。
        self.driver.quit()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass