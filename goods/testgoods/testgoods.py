from unittest import TestCase
import requests

a = ''
b = ''


class Test_city(TestCase):
    def test_0_getcity(self):
        url = 'http://127.0.0.1:8000/goods/gethome/'
        resp = requests.post(url ,data={'info_name':'超进口的水果'})
        # assert resp.json()['']
        a = resp.text


    # def test_1_getcity(self):
    #     url = 'http://127.0.0.1:8000/goods/gethome/'
    #     resp = requests.get(url)
    #     # assert resp.json()['']
    #     global a
    #     a = resp.json()
    #     print(a)

    def test_2_area(self):
        resp = requests.get(url=f'http://127.0.0.1:8000/goods/getcate/?oneid=b2703ac551c140b590231911cfe06900')



    def test_2_setcity(self):
        resp = requests.post(url=f'http://127.0.0.1:8000/goods/getinfo/?goods_code=xiagua02')
        # print(resp.json())



if __name__ == '__main__':
    TestCase().run()
