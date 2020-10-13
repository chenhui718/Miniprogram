import requests, app, logging


class OrderApi:
    def __init__(self):
        # 订单列表
        self.user_order_list_url = app.base_url + '/order/by_user?page=1'
        # 创建订单
        self.create_order_url = app.base_url + '/order'
        # 查看订单
        self.query_order_url = app.base_url + '/order/{}'

    def order_list_api(self, page=1):
        """订单列表"""
        # 参数
        logging.info('订单-订单列表')
        data = {'page': page}
        logging.info('请求参数：{}'.format(data))
        # 返回值
        return requests.get(self.user_order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        """创建订单"""
        # 数据
        logging.info('订单-订单列表')
        data = {"products": [{"product_id": product_id, "count": count}]}
        logging.info('请求参数：{}'.format(data))
        # 返回值
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_api(self, order_id):
        logging.info('订单-订单列表')
        """查询订单"""
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
