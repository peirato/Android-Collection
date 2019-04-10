#encoding:utf-8
import time
from appium import webdriver
import unittest
from ddt import ddt,data,unpack


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '090d0b62'
        desired_caps['appPackage'] = 'com.emingren.xuebang'
        desired_caps['appActivity'] = '.page.login.SplashActivity'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("1nrnsdf3r", "12nem,j3nre", False), ("13rf df12#@33", "7hebf87rh^%&", False), ("student3000", "666888", True))
    @unpack
    def testLogIn(self, username, password, expectedresule):

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

        self.driver.find_element_by_id("com.emingren.xuebang:id/et_login_activity_username").send_keys(username)
        self.driver.find_element_by_id("com.emingren.xuebang:id/et_login_activity_password").send_keys(password)
        self.driver.find_element_by_id("com.emingren.xuebang:id/btn_login_activity_login").click()

        try:
            if self.driver.find_element_by_id("com.emingren.xuebang:id/drawer_layout_home_page_fragment").is_displayed():
                exist = True
        except Exception :
            exist = False

        self.assertEqual(exist, expectedresule)

    def swipe_left(self):
        # width = self.manage().window().getSize().width
        # height = self.manage().window().getSize().height
        # width = self.driver.get_window_size('width')
        # height = self.driver.get_window_size('height')
        print(self.driver.get_window_size())
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print("width: " + str(width) + "height: " + str(height))
        self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, 300)
        print("向左滑动 from (width:" + str(width * 3 / 4) + ",height:" + str(height / 2) + ") to (width:" + str(
            width / 4) + ",height:" + str(height / 2)+")")

    def tearDown(self):
        self.driver.quit()
