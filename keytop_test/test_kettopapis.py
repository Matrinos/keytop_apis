import requests
from keytop_test.crypto import attachSignature
import uuid

base_url = "http://kp-open.keytop.cn/unite-api"
kytop_header = {"Content-Type": "application/json", "accept": "application/json", "charset": "UTF-8",
                "version": "1.0.0"}
app_secret = "f82b42c6f60246eba56ec4a77dfe7f9b"


def test_query_car_info():
    keytop_url = base_url + "/api/wec/QueryCarInfo"
    print("request: " + keytop_url)
    k_data = {"appId": "10749", "parkId": "4603", "serviceCode": "queryCarInfo", "plateNo": "123", "pageIndex": "1",
              "pageSize": "15", "reqId": str(uuid.uuid4())}
    json_body = attachSignature(k_data, app_secret)
    response_k = requests.post(keytop_url, headers=kytop_header, json=json_body)
    print(response_k.json())


def test_get_free_space_num():
    keytop_url = base_url + "/api/wec/GetFreeSpaceNum"
    print("request: " + keytop_url)
    k_data = {"appId": "10749", "parkId": "4603", "serviceCode": "getFreeSpaceNum", "reqId": str(uuid.uuid4())}
    json_body = attachSignature(k_data, app_secret)
    response_k = requests.post(keytop_url, headers=kytop_header, json=json_body)
    print(response_k.json())
