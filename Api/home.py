import logging

import requests, app


class HomeApi:
    def __init__(self):
        self.banner_url = app.base_url + '/banner/{}'
        self.theme_url = app.base_url + '/theme'
        self.recent_product_url = app.base_url + '/product/recent'

    def banner_api(self, num=1):
        """
        :param num: 轮播图数量
        :return:
        """
        logging.info('首页-轮播图')
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids='1,2,3'):
        """
        请求专题栏
        :param ids: 专题栏数量
        :return:
        """
        logging.info('首页-专题栏')
        data = {'ids': ids}
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """
        请求最近新品
        :return:
        """
        logging.info('首页-最近新品')
        return requests.get(self.recent_product_url)
