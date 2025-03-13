from wc_py.webcommander.auth.dto.token_dto import RequestTokenDTO
from wc_py.webcommander.categories.admin.admin_categories import AdminCategories
from wc_py.webcommander.blog.admin.admin_blog import AdminBlog
from wc_py.webcommander.currency.admin.admin_currency import AdminCurrency
from wc_py.webcommander.customers.admin.admin_customers import AdminCustomers
from wc_py.webcommander.orders.admin.admin_orders import AdminOrders
from wc_py.webcommander.discount.admin.admin_discount import AdminDiscount
from wc_py.webcommander.product.admin.admin_product import AdminProduct
from wc_py.webcommander.product.product import Product
from wc_py.webcommander.shipping_profiles.admin.admin_shipping_profiles import AdminShippingProfiles
from wc_py.webcommander.shipping_rates.admin.admin_shipping_rates import AdminShippingRates
from wc_py.webcommander.shipping_rules.admin.admin_shipping_rules import AdminShippingRules
from wc_py.webcommander.tax_codes.admin.admin_tax_codes import AdminTaxCodes
from wc_py.webcommander.tax_profiles.admin.admin_tax_profiles import AdminTaxProfiles
from wc_py.webcommander.tax_rules.admin.admin_tax_rules import AdminTaxRules
from wc_py.webcommander.tax_zones.admin.admin_tax_zones import AdminTaxZones
from wc_py.webcommander.settings.settings import Settings
from wc_py.webcommander.variation.admin.admin_variation import AdminVariation


class WebCommanderSDK:
    _request_token_dto: RequestTokenDTO = None
    product: Product = None
    admin_product: AdminProduct = None
    admin_customers: AdminCustomers = None
    admin_currency: AdminCurrency = None
    admin_orders: AdminOrders = None
    admin_categories: AdminCategories = None
    admin_tax_profiles: AdminTaxProfiles = None
    admin_tax_codes: AdminTaxCodes = None
    admin_tax_zones: AdminTaxZones = None
    admin_tax_rules: AdminTaxRules = None
    admin_shipping_profiles: AdminShippingProfiles = None
    admin_shipping_rules: AdminShippingRules = None
    admin_shipping_rates: AdminShippingRates = None
    admin_blog: AdminBlog = None
    admin_discount: AdminDiscount = None
    settings: Settings = None
    admin_variation: AdminVariation = None

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
        self.admin_customers = AdminCustomers(request_token_dto=self._request_token_dto)
        self.admin_orders = AdminOrders(request_token_dto=self._request_token_dto)
        self.admin_categories = AdminCategories(request_token_dto=self._request_token_dto)
        self.admin_tax_profiles = AdminTaxProfiles(request_token_dto=self._request_token_dto)
        self.admin_tax_codes = AdminTaxCodes(request_token_dto=self._request_token_dto)
        self.admin_tax_zones = AdminTaxZones(request_token_dto=self._request_token_dto)
        self.admin_tax_rules = AdminTaxRules(request_token_dto=self._request_token_dto)
        self.admin_shipping_profiles = AdminShippingProfiles(request_token_dto=self._request_token_dto)
        self.admin_shipping_rules = AdminShippingRules(request_token_dto=self._request_token_dto)
        self.admin_shipping_rates = AdminShippingRates(request_token_dto=self._request_token_dto)
        self.admin_discount = AdminDiscount(request_token_dto=self._request_token_dto)
        self.admin_currency = AdminCurrency(request_token_dto=self._request_token_dto)
        self.admin_blog = AdminBlog(request_token_dto=self._request_token_dto)
        self.settings = Settings(request_token_dto=self._request_token_dto)
        self.admin_variation = AdminVariation(request_token_dto=self._request_token_dto)

    def init_sdk(self, request_token_dto: RequestTokenDTO) -> 'WebCommanderSDK':
        self._request_token_dto = request_token_dto
        self._init_endpoints()
        return self
