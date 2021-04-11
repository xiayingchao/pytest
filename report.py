import unittest
from class202103271.cases.api_case import ApiCases
path = 'cases'

discover = unittest.defaultTestLoader.discover(path,'api_case.py')
with open('./reporta/report2.txt','w') as f :
    unittest.TextTestRunner(stream=f).run(discover)

##创建测试套件
suite = unittest.TestSuite()
#添加测试用例
suite.addTest(ApiCases('test_2_info'))
suite.addTest(ApiCases('test_6_order'))
suite.addTest(ApiCases('test_1_list'))
suite.addTest(ApiCases('test_3_list'))
xiugug
runner = unittest.TextTestRunner()
runner.run(suite)