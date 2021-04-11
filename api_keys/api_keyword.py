'''
    关键字封装
'''
import json
#这个地方要看一下
import jsonpath as jsonpath
import requests

class ApiKeys:
    #get请求
    def get(self,url,headers=None,data=None):
        return requests.get(url=url,headers=headers,params=data)
    #post请求
    def post(self,url,headers=None,data=None,json_=None):
        return requests.post(url=url,headers=headers,params=data,json=json_)
    ##提取需要被提取的内容作为被关联的值来进行保存，会应用到jsonpath
    #这个地方要看一下
    def get_text(self,res,key):
        if res is not None:
            try:

                text = json.loads(res)
                #了解jsonpath
                value = jsonpath.jsonpath(text,'$..{0}'.format(key))
                if value:
                    return value[0]
                else:
                    return value
            except Exception as e:
                return e
        else:
            return value


