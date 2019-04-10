#/usr/bin/python
#encoding:utf-8

import os
import time

def runCMD(cmd):

    return os.popen(cmd)

#按下电源按钮
def powerKey():

    print runCMD("adb shell input keyevent 26")

#启动应用
def startAPP():

    print runCMD("adb shell am start -W -n com.emingren.xuebang/.page.login.SplashActivity")

#结束应用 双击返回按钮
def killAPP():

    print runCMD("adb shell input keyevent 4")
    print runCMD("adb shell input keyevent 4")


startAPP()
time.sleep(3)
killAPP()



