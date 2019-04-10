# encoding:utf-8

import unitTestDome
import unittest


# mysuite = unittest.TestSuite()
# # 通过名称来查找用例
# mysuite.addTest(unitTestDome.MyTestCase("testLogin"))
# 通过名称来查找用例的方法在使用ddt后会失效

# 通过类来查找用例 在使用ddt后推荐使用这种方法来查找用例
cases = unittest.TestLoader().loadTestsFromTestCase(unitTestDome.MyTestCase)
mysuite = unittest.TestSuite([cases])

# 设置log等级
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
