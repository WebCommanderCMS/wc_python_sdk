from dataclasses import dataclass
from typing import List
from wc_py.sdlize.wc_base_dto import WCBaseDTO
from wc_py.webcommander.common.dto.common_dto import CommonStructureDTO, PaginationDTO


@dataclass(kw_only=True)
class ProductSettingsDataDTO(WCBaseDTO):
    labelForCallForPrice: str = None
    labelForExpectToPay: str = None
    labelForBasePrice: str = None
    addToCart: str = None
    variationOptionView: str = None


@dataclass(kw_only=True)
class SeoConfigDTO(WCBaseDTO):
    configKey: str = None
    metaTags: List[str] = None
    id: int = None
    type: str = None
    value: str = None
    version: str = None


@dataclass(kw_only=True)
class RelatedOrSimilarProductDTO(WCBaseDTO):
    id: int = None
    name: str = None
    url: str = None


@dataclass(kw_only=True)
class MediaDataDTO(WCBaseDTO):
    id: int = None
    filename: str = None
    link: str = None


@dataclass(kw_only=True)
class ImageDataDTO(MediaDataDTO):
    thumbnail: str = None


@dataclass(kw_only=True)
class VideoDataDTO(MediaDataDTO):
    thumbnail: str = None


@dataclass(kw_only=True)
class ProductMediaDTO(WCBaseDTO):
    images: list[ImageDataDTO] = None
    videos: list[VideoDataDTO] = None
    specs: list[MediaDataDTO] = None


@dataclass(kw_only=True)
class ParentDataDTO(WCBaseDTO):
    id: str = None
    name: str = None
    isInTrash: str = None
    isParentInTrash: str = None
    isDisposable: str = None


@dataclass(kw_only=True)
class ProductLayoutDataDTO(WCBaseDTO):
    id: str = None
    name: str = None


@dataclass(kw_only=True)
class WeekdaysDataDTO(WCBaseDTO):
    day: str = None
    startHour: int = None
    startMinute: int = None
    endHour: int = None
    endMinute: int = None


@dataclass(kw_only=True)
class ProductAvailableWeekdaysDataDTO(WCBaseDTO):
    enabled: bool = None
    weekdays: list[WeekdaysDataDTO] = None

@dataclass(kw_only=True)
class BaseProfileDTO(WCBaseDTO):
    id: int = None
    name: str = None


@dataclass(kw_only=True)
class ShippingProfileDataDTO(BaseProfileDTO):
    pass


@dataclass(kw_only=True)
class TaxProfileDataDTO(BaseProfileDTO):
    pass


@dataclass(kw_only=True)
class ProductPricingAndStockDTO(WCBaseDTO):
    availableStock: int = None
    enableCallForPrice: bool = None
    enableMultipleOrder: bool = None
    expectedToPay: bool = None
    expectedToPayPrice: float = None
    hidePrice: bool = None
    lowLevelStock: int = None
    maximumOrderQuantity: int = None
    minimumOrderQuantity: int = None
    multipleOrderQuantity: int = None
    onSale: bool = None
    onSalePrice: float = None
    onSalePriceType: str = None
    restrictPriceFor: str = None
    restrictPriceForExceptCustomers: List[str] = None
    restrictPurchaseFor: str = None
    restrictPurchaseForSelectedCustomers: List[str] = None
    shippingProfile: ShippingProfileDataDTO = None
    taxProfile: TaxProfileDataDTO = None
    trackInventory: bool = None


@dataclass(kw_only=True)
class ProductDataDTO(WCBaseDTO):
    administrativeStatus: bool = None
    advanced: str = None
    available: str = None
    availableFor: str = None
    availableFromDate: str = None
    availableStock: int = None
    availableToDate: str = None
    availableOnDateRange: str = None
    availableOnWeekdays: ProductAvailableWeekdaysDataDTO = None
    basePrice: float = None
    costPrice: float = None
    customClass: float = None
    customProperties: str = None
    heading: str = None
    id: str = None
    imageAndVideo: ProductMediaDTO = None
    isOnSale: bool = None
    name: str = None
    parents: list[ParentDataDTO] = None
    password: str = None
    passwordProtected: str = None
    productPricingAndStock: ProductPricingAndStockDTO = None
    productLayout: CommonStructureDTO = None
    productSummary: str = None
    productDescription: str = None
    productPage: str = None
    productType: str = None
    restrictPriceFor: str = None
    restrictPurchaseFor: str = None
    restrictForSelectedCustomers: List[str] = None
    relatedProducts: list[RelatedOrSimilarProductDTO] = None
    similarProducts: list[RelatedOrSimilarProductDTO] = None
    selectedCustomers: List[str] = None
    salePrice: float = None
    seoConfigs: list[SeoConfigDTO] = None
    sku: str = None
    summary: str = None
    tags: list[str] = None
    url: str = None
    videos: List[str] = None


@dataclass(kw_only=True)
class ProductResponseDTO(WCBaseDTO):
    status: str = None
    product: ProductDataDTO = None


@dataclass(kw_only=True)
class ProductListResponseDTO(WCBaseDTO):
    products: list[ProductDataDTO] = None
    pagination: PaginationDTO = None
