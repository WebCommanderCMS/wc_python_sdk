from wc_py.webcommander.auth.dto.token_dto import RequestTokenDTO
from wc_py.webcommander.product.admin.admin_product import AdminProduct
from wc_py.webcommander.product.product import Product


class WebCommanderSDK:
    _request_token_dto: RequestTokenDTO = None
    product: Product = None
    admin_product: AdminProduct = None

    def __init__(self, webcommander_url: str = None, client_id: str = None, client_secret: str = None,
                 redirect_uri: str = None,
                 grant_type: str = None, auth_string: str = None):
        if client_secret and client_id and redirect_uri and auth_string:
            self._request_token_dto = RequestTokenDTO(
                webCommanderUrl=webcommander_url,
                clientId=client_id,
                clientSecret=client_secret,
                redirectUri=redirect_uri,
                grantType=grant_type,
                authString=auth_string
            )
            self._init_endpoints()

    def _init_endpoints(self):
        self.product = Product(request_token_dto=self._request_token_dto)
        self.admin_product = AdminProduct(request_token_dto=self._request_token_dto)

    def init_sdk(self, request_token_dto: RequestTokenDTO) -> 'WebCommanderSDK':
        self._request_token_dto = request_token_dto
        self._init_endpoints()
        return self
