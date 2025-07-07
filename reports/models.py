from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OfferItemData:
    """Класс для хранения данных предложения."""

    price: Decimal | None = None
    price_no_vat: Decimal | None = None
    own_currensie: str | None = None
    own_currensie_rate: Decimal | None = None
    is_winner: bool = False


@dataclass
class ReportRow:
    """Класс для хранения строки отчета."""

    tender_name: str
    values: tuple[OfferItemData]


@dataclass
class ReportData:
    """Класс для хранения данных отчета."""

    headers: tuple[str]
    rows: tuple[ReportRow]
