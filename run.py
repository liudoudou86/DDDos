# -*- coding:utf-8 -*-

import requests
import threading

host = "http://www.sy-angel.com/"
session = requests.session()

def go():  
    url = host
    headers = {"Content-Type":"application/json"}
    res = session.request(url = url,method='get',headers = headers)
    status_code=res.status_code # 获取响应状态码
    # print('响应状态码:{}'.format(status_code))


if __name__=="__main__":
    for i in range(10):
        t=threading.Thread(target=go,name="thread-"+str(i))
        t.start()
        t.join()