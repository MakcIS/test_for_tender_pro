from domain.entities.tender import TenderEntity
from dto.api.tender import TenderItem


class TenderMapper:
    """Класс для маппинга тендера."""

    @staticmethod
    def to_entity(tender: TenderItem) -> TenderEntity:
        return TenderEntity(
            tender_id=tender['tender_id'],
            name=tender["name"],
            amount=tender["amount"],
            winner_id=tender.get("winnerid", None)
        )
    
    @staticmethod
    def list_dto_to_entity(self, tenders: list[TenderItem]) -> list[TenderEntity]:
        return [self.to_entity(tender) for tender in tenders]