from Api.apiFactory import ApiFactory
import app, utils,logging
import pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        res = ApiFactory.get_user_api().get_token_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json().get('token')) > 0
        app.headers['token'] = res.json().get('token')
        print('app.headers:{}'.format(app.headers))

    def test_verify_token(self):
        """响应"""
        res = ApiFactory.get_user_api().verify_token_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get('isValid') is True

    def test_user_addr(self):
        """用户地址"""
        # 获取响应
        res = ApiFactory.get_user_api().user_addr_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ['上海市', '浦东新区', '大白', '001号', '15962620132']]
