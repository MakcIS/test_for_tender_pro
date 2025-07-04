from dataclasses import dataclass

@dataclass
class Offer:
    """Сущность участника тендера (offer)."""
    id: int
    offer_id: int
    own_currensie: str
    title: str = ""
    vat: str = ""

@dataclass
class OfferItem:
    """Сущность позиции предложения (offer item)."""
    id: int
    offer_id: int
    item_id: int
    own_currensie: str
    own_currensie_rate: str
    price: str
    price_no_vat: str