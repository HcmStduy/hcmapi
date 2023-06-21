from unittest import TestCase
import requests


a = ''
b = ''


class Test_city(TestCase):
    # def test_0_getcart(self):
    #     url = 'http://127.0.0.1:8000/cart/getcart/'
    #     resp = requests.post(url,data={
    #         'goods_id':'3fa60be34cad4f1d8359402892546e60',
    #         'user_id':'2f51eaa079f8421f86c73e051903a422'
    #     })
    #
    #     print(resp.json())
    # def test_0_getcart(self):
    #     url = 'http://127.0.0.1:8000/cart/addsuborder/'
    #     resp = requests.post(url,data={
    #         'goods_id':'3fa60be34cad4f1d8359402892546e60',#7221f54340d9494b96cee374e5dafc143fa60be34cad4f1d8359402892546e60
    #         'user_id':'2f51eaa079f8421f86c73e051903a422',
    #         'sub_goods':1
    #     })
    #     # assert resp.json()['']
    #     print(resp.json())
    # def test_0_getcart(self):
    #     url = 'http://127.0.0.1:8000/cart/orderdown/'
    #     resp = requests.post(url, data={
    #         'goods_id': '3fa60be34cad4f1d8359402892546e60',
    #         # 7221f54340d9494b96cee374e5dafc143fa60be34cad4f1d8359402892546e60
    #         'user_id': '2f51eaa079f8421f86c73e051903a422',
    #         'order_num': 1,
    #         'address':'新疆',
    #         'name':'hhh',
    #         'phone':'1234567890'
    #     })
    #
    #     print(resp.json())
    def test_1_getcart(self):
        url = 'http://127.0.0.1:8000/cart/sum/'
        resp = requests.post(url, data={
            'user_id': '2f51eaa079f8421f86c73e051903a422',
        })

        print(resp.json())


if __name__ == '__main__':
    TestCase().run()
