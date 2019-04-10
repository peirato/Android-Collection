# /usr/bin/python
# encoding:utf-8

import csv
import os
import time

PACKAGE_NAME = "com.emingren.xuebang"
LAUNCH_ACTIVITY = ".page.login.SplashActivity"


class App(object):

    def __init__(self):
        self.content = ""
        self.startTime = 0

    # 启动app
    def LaunchApp(self):

        cmd = "adb shell am start -W -n " + PACKAGE_NAME + "/" + LAUNCH_ACTIVITY
        self.content = os.popen(cmd)

    # 停止app
    def StopApp(self):

        cmd = "adb shell am force-stop " + PACKAGE_NAME
        os.popen(cmd)

    # 获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

    # 控制类
    class Controller(object):

        # 获取app的实例
        def __init__(self, count):
            self.app = App()
            self.counter = count
            self.alldata = [("timestamp", "elapsedtime")]

        # 单次测试过程
        def testprocess(self):
            self.app.LaunchApp()
            elpasedtime = self.app.GetLaunchedTime()
            self.app.StopApp()
            currenttime = self.getCurrentTime()
            self.alldata.append((currenttime, elpasedtime))

        # 多次执行测试过程
        def run(self):
            while self.counter > 0:
                self.testprocess()
                self.counter = self.counter - 1

        def getCurrentTime(self):
            currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return currentTime

        # 数据的存储
        def saveDataToCSV(self):
            csvfile = file('startTime.csv', 'wb')
            writer = csv.writer(csvfile)
            print(self.alldata)
            writer.writerows(self.alldata)
            csvfile.close()

    if __name__ == "__main__":
        controller = Controller(10)
        controller.run()
        controller.saveDataToCSV()
