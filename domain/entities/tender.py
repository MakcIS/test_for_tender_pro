from dataclasses import dataclass


@dataclass
class TenderEntity:
    """Сущность тендера."""
    tender_id: int
    name: str
    amount: str
    winner_id: str | None = None