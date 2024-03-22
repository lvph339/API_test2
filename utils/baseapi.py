import requests
from utils.Logger import Log

log = Log()

class Baseapi:
    #获取token
    @classmethod
    def get_token(cls):
        header = {'登录信息key': '登录信息value'}#获取或者写死
        return header

    #发送请求
    @classmethod
    def send(cls, url, method, cookie, headers, param):
        #判断请求方法
        if method == 'get':
            response = requests.request(url, method, cookie, headers, params=param)
        elif method == 'post':
            response = requests.request(url, method,  cookie, headers, json=param)
        # 输出日志信息
        log.info(f"response={response.json()}")
        # 返回响应信息
        return response
