from tests.common.common_data import CommonData
from wc_py.common.sdk_conf import SDKConfig
from wc_py.common.wc_exception import WCException
from wc_py.webcommander.webcommander_sdk import WebCommanderSDK


def admin_product_get_list_test():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True

    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.admin_product.list(max="2")
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def admin_product_get_info_test():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.admin_product.info(id="55")
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


def admin_product_get_count_test():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = True
    webcommander_sdk: WebCommanderSDK = WebCommanderSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        response = webcommander_sdk.admin_product.count()
        print(response)
    except WCException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)


admin_product_get_count_test()
admin_product_get_info_test()
admin_product_get_list_test()
