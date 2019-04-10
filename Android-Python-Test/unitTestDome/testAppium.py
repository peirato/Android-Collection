# encoding:utf-8

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = '090d0b62'
desired_caps['appPackage'] = 'com.emingren.xuebang'
desired_caps['appActivity'] = '.page.login.SplashActivity'
desired_caps['unicodeKeyboard'] = "True"
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

driver.find_element_by_id("et_login_activity_username").send_keys('student3000')
driver.find_element_by_id("et_login_activity_password").send_keys('666888')
driver.find_element_by_id("btn_login_activity_login").click()

try:
    if driver.find_element_by_id("btn_login_activity_login").is_displayed():
       print "fail"
except Exception, e:
        print e
        print "pass"

driver.quit()

time.sleep(5)

