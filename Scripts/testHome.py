import utils, logging
from Api.apiFactory import ApiFactory


class TestHomeApi:
    def test_home_api(self):
        """轮播图"""
        # 请求返回数据
        respond = ApiFactory.get_home_api().banner_api()
        logging.info('请求地址：{}'.format(respond.url))
        logging.info('响应数据：{}'.format(respond.json()))
        # 断言状态码
        utils.common_assert_code(respond)
        # 断言id和name
        assert respond.json().get('id') == 1 and respond.json().get('name') == '首页置顶'
        # 断言长度
        assert len(respond.json().get('items')) > 0

    def test_theme_api(self):
        """专题栏"""
        # 请求数据
        respond = ApiFactory.get_home_api().theme_api()
        logging.info('请求地址：{}'.format(respond.url))
        logging.info('响应数据：{}'.format(respond.json()))
        # 断言状态码
        utils.common_assert_code(respond)
        # 断言三个 id = 1， 2， 3
        assert 'id":1' in respond.text and 'id":2' in respond.text and 'id":3' in respond.text
        # 断言关键字段 name description head_img topic_img
        assert False not in [i in respond.text for i in ['name', 'description', 'head_img', 'topic_img']]

    def test_recent_api(self):
        """最近新品"""
        # 请求数据
        respond = ApiFactory.get_home_api().recent_product_api()
        logging.info('请求地址：{}'.format(respond.url))
        logging.info('响应数据：{}'.format(respond.json()))
        # 断言状态码
        utils.common_assert_code(respond)
        # 断言关键字段 id name main_img_url
        assert 'id' in respond.text and 'name' in respond.text and 'main_img_url' in respond.text
        # 断言长度
        assert len(respond.json()) > 0
