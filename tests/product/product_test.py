from tests.common.common_data import CommonData
from wc_py.common.wc_exception import WCException
from wc_py.webcommander.webcommander_sdk import WebCommanderSDK


def product_get_list_test():
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.product.list(max="2")
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def product_get_info_test():
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.product.info(id="55")
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def product_get_count_test():
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.product.count()
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def product_get_settings_test():
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.product.settings()
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


product_get_count_test()
product_get_info_test()
product_get_list_test()
product_get_settings_test()
