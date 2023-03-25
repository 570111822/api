import requests
import pytest


def test_login():
    url = 'https://student.72crm.com/api-11/login'
    json = {"username": "13888888888", "password": "like;314"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=json, headers=headers)
    assert res.status_code == 200
    assert res.json()['code'] == 0
    assert res.json()['msg'] == 'success'
    assert 'adminToken' in res.json()['data']
    return res.json()['data']['adminToken']


def test_select_customer_list():
    token = test_login()
    url = 'https://student.72crm.com/api-11/crmCustomer/queryPageList'
    json = {"search": "", "type": 2, "sceneId": "1628776974541824000", "page": 1, "limit": 10}
    headers = {"Admin-Token": token}
    res = requests.post(url, json=json, headers=headers)
    # print(res.json())
    assert res.json()['code'] == 0
    assert res.json()['msg'] == 'success'

if __name__ == '__main__':
    pytest.main(['-vs', 'test_crm_api.py'])

