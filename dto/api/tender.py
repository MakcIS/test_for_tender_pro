from typing import TypedDict


class TenderItem(TypedDict, total=False):
    """
    Описание структуры позиции конкурса (tender item) по контракту.
    """

    id: int  # Внутренний ID позиции
    tender_id: int  # ID конкурса
    number: int  # Порядковый номер позиции
    name: str  # Наименование позиции
    description: str  # Описание позиции
    amount: str  # Количество (строка для точности)
    unit_name: str  # Единица измерения
    vat: str | None  # Ставка НДС
    winnerid: str | None  # ID победителя (если есть)
    custom_field: str  # Пользовательское поле
