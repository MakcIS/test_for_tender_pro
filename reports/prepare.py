from domain.entities.offer import OfferEntity, OfferItemEntity
from domain.entities.tender import TenderEntity
from reports.models import OfferItemData, ReportData, ReportRow


class DataPreparer:
    def __init__(
        self,
        offers: list[OfferEntity],
        offer_items: dict[int : list[OfferItemEntity]],
        tenders: list[TenderEntity],
    ):
        self.offers = offers
        self.offer_items = offer_items
        self.tenders = tenders

    @staticmethod
    def finder_winner(values: list[OfferItemData]) -> None:
        """Метод для поиска победителя в списке предложений."""
        min_price = min(
            value.price * value.own_currensie_rate
            for value in values
            if value.price is not None
        )
        for value in values:
            if (
                value is not None
                and value.price * value.own_currensie_rate == min_price
            ):
                value.is_winner = True

    def get_data(self) -> ReportData:
        """Формирует данные для построения таблицы."""
        headers = tuple(["Позиция"] + [offer.title for offer in self.offers])
        rows = []

        for tender in self.tenders:
            values = []
            for offer in self.offers:
                items = filter(
                    lambda i: i.item_id == tender.tender_id,
                    self.offer_items.get(offer.offer_id, []),
                )
                if items:
                    for item in items:
                        values.append(
                            OfferItemData(
                                price=item.price,
                                price_no_vat=item.price_no_vat,
                                own_currensie=item.own_currensie,
                                own_currensie_rate=item.own_currensie_rate,
                                is_winner=str(offer.offer_id) == tender.winner_id,
                            )
                        )
                else:
                    values.append(OfferItemData())
            if not tender.winner_id:
                self.finder_winner(values)

            rows.append(ReportRow(tender_name=tender.name, values=tuple(values)))

        return ReportData(headers=headers, rows=tuple(rows))
