#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_desired_capabilities():

    desired_caps = {

        'platformName': 'Android',

        'platformVersion': '4.0.4',

        'deviceName': 'V889F',

        'appPackage': 'com.alibaba.mts.mtsdemoapp',

        'appWaitPackage': 'com.alibaba.mts.mtsdemoapp',

        'app': "D:/home/mdp/result/GroovyTest/case1/task.apk",

        'newCommandTimeout': 30,

        'automationName': 'Appium'

    }

    return desired_caps


def get_uri():
    return "http://localhost:50000/wd/hub"
