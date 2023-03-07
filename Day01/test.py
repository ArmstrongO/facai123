# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
from importlib import reload


reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ttsapi'
APP_KEY = '6048390e9b1bd0d4'
APP_SECRET = 'YZcsB83FD3HZsNNikQKuDMiWFit5hvWN'


def encrypt(signstr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signstr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    q = "你好,本音频来自有道词典，通过Python接口调用生产"

    data = {'langType': 'zh-CHS'}
    salt = str(uuid.uuid1())
    signstr = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(signstr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    contenttype = response.headers['Content-Type']
    if contenttype == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filepath = "测试语音包" + str(millis) + ".mp3"
        fo = open(filepath, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        print(response.content)


if __name__ == '__main__':
    connect()