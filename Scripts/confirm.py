from Api.apiFactory import ApiFactory

# # 调用轮播图api
# print(f'轮播图：{ApiFactory.get_home_api().banner_api().json()}')
#
# # 调用主题
# print('调用主题：{}'.format(ApiFactory.get_home_api().theme_api().json()))
#
# # 调用最近新品
# print('最近新品：{}'.format(ApiFactory.get_home_api().recent_product_api().json()))

# 调用商品分类
# print('商品分类：{}'.format(ApiFactory.get_product_api().product_classify_api().json()))
# print('分类商品：{}'.format(ApiFactory.get_product_api().clssify_product_api().json()))
# print('商品信息：{}'.format(ApiFactory.get_product_api().product_info_api().json()))

# print('获取token：{}'.format(ApiFactory.get_user_api().get_token_api().json()))
print('订单列表：{}'.format(ApiFactory.get_order_api().order_list_api().json()))
print('创建订单：{}'.format(ApiFactory.get_order_api().create_order_api(12, 7).json()))
print('查询订单：{}'.format(ApiFactory.get_order_api().query_order_api(109).json()))
print('订单列表：{}'.format(ApiFactory.get_order_api().order_list_api().json()))
