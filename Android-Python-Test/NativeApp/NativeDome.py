# encoding:utf-8
import unittest
from appium import webdriver
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '090d0b62'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def test_something(self):
    #     self.assertEqual(True, False)

    def testAdd(self):
        # 定位
        number8 = self.driver.find_element_by_id("com.android.calculator2:id/digit_8")
        # 操作
        number8.click()

        addopertion = self.driver.find_element_by_id("com.android.calculator2:id/op_add")
        addopertion.click()
        number5 = self.driver.find_element_by_id("com.android.calculator2:id/digit_5")
        number5.click()
        equal = self.driver.find_element_by_id("com.android.calculator2:id/eq")
        equal.click()
        time.sleep(1)

        # 验证
        try:
            result = self.driver.find_element_by_id("com.android.calculator2:id/result")
            value = result.text
            self.assertEquals("13", value)
        except Exception:
            print "出现异常"
            self.fail("出现异常")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
