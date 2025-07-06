from domain.entities.offer import OfferEntity, OfferItemEntity
from domain.entities.tender import TenderEntity
from reports.models import OfferItemData, ReportData, ReportRow


class DataPreparer:
    def __init__(self,
                 offers:list[OfferEntity],
                 offer_items:dict[int:list[OfferItemEntity]],
                 tenders:list[TenderEntity]):
        self.offers = offers
        self.offer_items = offer_items
        self.tenders = tenders

    def get_data(self) -> ReportData:
        """ Формирует данные для построения таблицы. """
        headers = tuple(offer.title for offer in self.offers)
        rows = []

        for tender in self.tenders:
            values = []
            for offer in self.offers:
                for item in self.offer_items.get(offer.offer_id, [None]):
                    if item is None:
                        values.append(OfferItemData())
                        continue
                    values.append(OfferItemData(
                        price=item.price,
                        price_no_vat=item.price_no_vat,
                        own_currensie=item.own_currensie,
                        own_currensie_rate=item.own_currensie_rate,
                        is_winner=(offer.offer_id == tender.winnerid)
                    ))
            rows.append(ReportRow(tender_name=tender.name, values=tuple(values)))
                

        return ReportData(headers=headers, rows=tuple(rows))
        