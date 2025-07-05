from decimal import Decimal

from domain.entities.offer import OfferItemEntity, OfferEntity
from dto.api.offer import OfferItem, Offer

class OfferMapper:
    """Класс для маппинга участника."""

    @staticmethod
    def to_entity(offer: Offer) -> OfferEntity:
        return OfferEntity(
            id=offer['id'],
            offer_id=offer['offer_id'],
            own_currensie=offer['own_currensie'],
            title=offer['title'],
        )
    
    @staticmethod
    def list_dto_to_entity(offers: list[Offer]) -> list[OfferEntity]:
        return [OfferMapper.to_entity(offer) for offer in offers]
        

class OfferItemMapper:
    """Класс для маппинга предложений."""

    @staticmethod
    def to_entity(offer_item: OfferItem) -> OfferItemEntity:
        own_currensie_rate = Decimal(offer_item['own_currensie_rate'])
        price = Decimal(offer_item['price'])
        price_no_vat = Decimal(offer_item['price_no_vat'])

        return OfferItemEntity(
                id=offer_item['id'],
                offer_id=offer_item['offer_id'],
                item_id=offer_item['item_id'],
                own_currensie=offer_item['own_currensie'],
                own_currensie_rate=own_currensie_rate,
                price=price,
                price_no_vat=price_no_vat
        )

    @staticmethod
    def list_dto_to_entity(offer_items: list[OfferItem]) -> list[OfferItemEntity]:
        return [OfferItemMapper.to_entity(offer_item) for offer_item in offer_items]   