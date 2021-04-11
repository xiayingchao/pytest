import json
import unittest

from class202103271.api_keys.api_keyword import ApiKeys
from ddt import ddt,file_data

@ddt
class ApiCases(unittest.TestCase):
    #定义一个赋值函数，减少代码量
    def assignment(self,kwargrs):
        for key,value in kwargrs.items():
            if type(value) is dict:
                self.assignment(value)
            else :
                if value:
                    pass
                else:
                    kwargrs[key] = getattr(self,key)
        return kwargrs

    #此处不懂 定义一个全局变量，以便于这个变量可以再全局里面去用 一般定义再下面这个方法里面
    #初始化一批类成员 只运行一次
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://uat-sj-gateway.aihuishou.com'
        cls.ak= ApiKeys()
        cls.token = None
        cls.itemClusterNo = None
        cls.headers = {
            "Access-Token": "7a61f9e7791c8fdd6e82e409dcc06136"
        }
        cls.platformItemNo = None
        cls.saleNo = None
        cls.receiveAddressId = None
    #测试用例
    @file_data('../data/user.yaml')
    def test_1_list(self,**kwargs):
        url = self.url + kwargs['path']
        data = kwargs['page']
        res = self.ak.post(url=url,json_=data)
        itemClusterNo = self.ak.get_text(res.text, kwargs['itemClusterNo'])
        if itemClusterNo:
            ApiCases.itemClusterNo = itemClusterNo
        print(res.text)
        #这个断言要看一下 断言的语法部分要恶补
        #self.assertTrue(itemClusterNo)
    def test_2_info(self):
        url = self.url + '/recycler-api/fixed-sale/v3/item/list'
        data = {
            "itemClusterNo":self.itemClusterNo,
            "pageSize":20,
            "pageIndex":0,
            "levelPpnList":[]
        }
        res = self.ak.post(url=url, headers=self.headers, json_=data)
        platformItemNo = self.ak.get_text(res.text,'platformItemNo')
        if platformItemNo:
            ApiCases.platformItemNo = platformItemNo
        print(res.text)
    def test_3_addshopping(self):
        url = self.url + '/recycler-api/shopping/cart/add'
        data =  {
            "platformItemNo":self.platformItemNo,
            "quantity":1
        }
        res = self.ak.post(url=url,headers=self.headers,json_=data)
        print(res.text)
    def test_4_submits(self):
        url = self.url + '/recycler-api/shopping/cart/buy/submit'
        data = {"platformItemNos":[self.platformItemNo]}
        res = self.ak.post(url=url,headers=self.headers,json_=data)
        ApiCases.saleNo = self.ak.get_text(res.text,'data')
        print(res.text)
    def test_5_address(self):
        url = self.url + '/sj-api/recycler/deliveries'
        res = self.ak.get(url=url,headers=self.headers)
        ApiCases.receiveAddressId = self.ak.get_text(res.text,'deliveryId')
        print(res.text)
    @file_data('../data/order.yaml')
    def test_6_order(self,**kwargs):
        dict_ = self.assignment(kwargs)
        url = self.url + dict_['path']
        res = self.ak.post(url=url,headers=self.headers,json_=dict_['data'])
        print(res.text)
##不太懂为啥有main函数就被调用了
if __name__ == '__main__':
    unittest.main()

