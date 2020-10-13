from Api.home import HomeApi
from Api.product import ProductApi
from Api.user import Userapi
from Api.order import OrderApi


class ApiFactory:
    @classmethod
    def get_home_api(cls):
        return HomeApi()

    @classmethod
    def get_product_api(cls):
        return ProductApi()

    @classmethod
    def get_user_api(cls):
        return Userapi()

    @classmethod
    def get_order_api(cls):
        return OrderApi()
