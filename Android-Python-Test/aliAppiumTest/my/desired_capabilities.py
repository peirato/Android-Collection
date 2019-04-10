#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_desired_capabilities():

        desired_caps = {

            'platformName': 'Android',

            'platformVersion': "7.1",

            'deviceName': '090d0b62',

            'appPackage': 'com.emingren.xuebang',

            'appWaitPackage': 'com.emingren.xuebang',

            'app': "E:/AppTest/test.apk",

            'newCommadTimeout': 30,

            'automationName': 'Appium'

        }

        return desired_caps

def get_uri():

    return "http://localhost:4723/wd/hub"
