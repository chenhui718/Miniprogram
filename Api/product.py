import app, requests,logging


class ProductApi:

    def __init__(self):
        self.product_classify_url = app.base_url + '/category/all'
        self.clssify_product_url = app.base_url + '/product/by_category'
        self.product_info_url = app.base_url + '/product/{}'

    def product_classify_api(self):
        logging.info('商品-商品分类')
        """商品分类"""
        return requests.get(self.product_classify_url)

    def clssify_product_api(self, classify_id=2):
        """
        分类下商品
        :param id: 分类商品id
        :return: 返回商品分类数据
        """
        logging.info('商品-分类下商品')
        data = {"id": classify_id}
        logging.info('请求参数：{}'.format(data))
        return requests.get(self.clssify_product_url, params=data)

    def product_info_api(self,product_id=2):
        """商品信息"""
        logging.info('商品-商品信息')
        return requests.get(self.product_info_url.format(product_id))
