import utils, logging
from Api.apiFactory import ApiFactory


class TestProductApi:

    def test_product_classify_api(self):
        res = ApiFactory.get_product_api().product_classify_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json()) > 0
        assert 'id' in res.text and 'name' in res.text

    def test_classify_product_api(self):
        res = ApiFactory.get_product_api().clssify_product_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ['id', 'name', 'price']]

    def test_product_info(self):
        res = ApiFactory.get_product_api().product_info_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get('id') == 2
        assert res.json().get('price') == '0.01'
