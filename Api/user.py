import logging

import requests, app


class Userapi:
    def __init__(self):
        self.get_token_url = app.base_url + '/token/user'
        self.token_verify_url = app.base_url + '/token/verify'
        self.user_addr_url = app.base_url + '/address'

    def get_token_api(self):
        """获取token"""
        # 获取code
        logging.info('用户-获取token')
        data = {'code': app.code}
        logging.info('请求参数：{}'.format(data))
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        """验证token"""
        # 获取token
        logging.info('用户-验证token')
        data = {'token': app.headers.get('token')}
        logging.info('请求参数：{}'.format(data))
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_addr_api(self):
        """获取地址信息"""
        logging.info('用户-获取地址信息')
        data = {'token': app.headers.get('token')}
        logging.info('请求参数：{}'.format(data))
        return requests.get(self.user_addr_url, headers=data)
