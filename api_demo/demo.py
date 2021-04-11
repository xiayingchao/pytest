'''
    基本的API关联测试代码

'''
#获取一口价列表
import requests,json

url_list = 'http://uat-sj-gateway.aihuishou.com/recycler-api/fixed-sale/v3/cluster/list'
data = {
    "pageSize":20,
    "pageIndex":10000
}
res = requests.post(url=url_list,json=data)
print(res.text)
#此处需要进一步学习
itemClusterNo = json.loads(res.text)['data'][1]['itemClusterNo']
print(itemClusterNo)

#查询平台商品
url_info = 'http://uat-sj-gateway.aihuishou.com/recycler-api/fixed-sale/v3/cluster/info'

headers = {
    "Access-Token":"7a61f9e7791c8fdd6e82e409dcc06136"
}

data = {
    "levelPpnList":[],
    "itemClusterNo":itemClusterNo
}

res2 = requests.post(url=url_info,headers=headers,json=data)
print(res2.text)