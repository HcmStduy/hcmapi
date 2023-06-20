from unittest import TestCase
import requests

a = ''
b = ''


class Test_city(TestCase):
    def test_0_getcity(self):
        resp = requests.get(url='http://127.0.0.1:8000/citys/getcity/')
        # assert resp.json()['']
        global a
        a = resp.json()['data']['A'][0][0]['id']
        print(a)

    def test_1_area(self):
        resp = requests.get(url=f'http://127.0.0.1:8000/citys/area/?city_id={a}')
        print(resp.json()['data'][0]['id'])
        global b
        b = resp.json()['data'][0]['id']

    def test_2_setcity(self):
        resp = requests.get(url=f'http://127.0.0.1:8000/citys/setcity/?area_id={b}')
        print(resp)



if __name__ == '__main__':
    TestCase().run()
