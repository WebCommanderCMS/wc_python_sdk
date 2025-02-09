from wc_py.common.sdk_util import SDKUtil
from wc_py.http.wc_rest_processor import WCRestProcessor
from wc_py.webcommander.common.common_enum import SortDirection
from wc_py.webcommander.common.dto.common_dto import CountResponseDTO
from wc_py.webcommander.common.dto.product_dto import ProductListResponseDTO, ProductResponseDTO, ProductSettingsDataDTO
from wc_py.webcommander.product.admin.admin_product_api_url import AdminProductApiUrl


class AdminProduct(WCRestProcessor):

    def list(self, max: str = None, offset: int = None, direction: SortDirection = None,
             order_by: str = None) -> ProductListResponseDTO:
        params = SDKUtil.init_pagination_params(max=max, offset=offset, direction=direction, order_by=order_by)
        response = self.get(url=AdminProductApiUrl.PRODUCT_LIST, params=params, response_obj=ProductListResponseDTO())
        return response

    def info(self, id: str = None) -> ProductResponseDTO:
        response = self.get(url=AdminProductApiUrl.PRODUCT_INFO.format(product_id=id),
                            response_obj=ProductResponseDTO())
        return response

    def count(self) -> CountResponseDTO:
        response = self.get(url=AdminProductApiUrl.PRODUCT_COUNT, response_obj=CountResponseDTO())
        return response
