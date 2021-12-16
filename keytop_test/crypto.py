import time
import hashlib

def md5(str_input):
    m = hashlib.md5()
    m.update(str_input.encode('utf-8'))
    return m.hexdigest()


def encryptMap(maps):
    keys = sorted(maps.keys())
    str_exp = ""
    for key in keys:
        value = maps[key]
        if key != "appId":
            if (type(value) == dict):
                str_exp += key + "={" + encryptMap(value) + "}&"
            elif (type(value) == list):
                str_exp += key + "=[" + encryptlist(value) + "]&"
            elif (value != None):
                str_exp += key + "=" + str(value) + "&"
    return str_exp.strip('&')


def encryptValue(value):
    if (type(value) == dict):
        return "{" + encryptMap(value) + "}"
    elif (type(value) == list):
        return "[" + encryptlist(value) + "]"
    elif (value != None):
        return str(value)


def encryptlist(lst):
    return ','.join(list(map(encryptValue, lst)))


def attachSignature(params, app_sercert):
    params_new = params.copy()
    time_stamp = time.time()  # 时间戳获取
    ts = str(int(round(time_stamp * 1000)))
    params_new['ts'] = ts
    exp_str = encryptValue(params_new)
    exp_str = exp_str.strip("{").strip("}")
    exp_str = exp_str + "&" + app_sercert
    sig_str = md5(exp_str).upper()
    # return sig_str
    params_new['key'] = sig_str
    return params_new

if __name__ == "__main__":
    input_param = {"amount": 100, "orderNo": "闽C12345", "payTime": "2020-03-06 10:57:22",
     "freeDetail": "[{\"code\":\"\",\"money\":100,\"time\":0,\"type\":0}]", "paySource": "EED96C219E83450A",
     "outOrderNo": "T20200306124536001", "parkId": "1000001", "payableAmount": 200,
     "reqId": "748584ae47104b0ab239732767ddc679", "payType": 1006, "payMethod": 6, "appId": "EED96C219E83450A",
     "freeTime": 0, "paymentExt": "{\"deviceNo\":\"123456\"}", "freeMoney": 100, "ts": 1583464576264}
    app_secret = "85d15350778b11e9bbaa506b4b2f6421"
    actual_code = attachSignature(input_param, app_secret)
    exp_code = "55B3663F1A4DB9CEE91EA0A28E43D428"
    assert(actual_code == exp_code)

