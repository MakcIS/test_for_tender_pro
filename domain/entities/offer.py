from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OfferEntity:
    """Сущность участника тендера."""

    id: int
    offer_id: int
    own_currensie: str
    title: str = ""


@dataclass
class OfferItemEntity:
    """Сущность позиции предложения."""

    id: int
    offer_id: int
    item_id: int
    own_currensie: str
    own_currensie_rate: Decimal
    price: Decimal
    price_no_vat: Decimal
