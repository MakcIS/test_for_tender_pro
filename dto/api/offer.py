from typing import TypedDict


class Offer(TypedDict, total=False):
    """
    Описание структуры элемента предложения (offer) по контракту get_offers.
    Все поля соответствуют данным, возвращаемым API.
    """

    id: int  # Внутренний ID записи
    offer_id: int  # ID предложения
    company_email: str  # Email компании
    date_spec: str  # Дата подачи предложения
    address: str  # Адрес
    own_currensie: str  # Валюта
    tare_cost: float | None  # Стоимость тары
    authorizedface_comment: str | None  # Комментарий уполномоченного лица
    is_rejected: int  # Признак отклонения (0/1)
    reason_id: int | None  # ID причины отклонения
    reason_comment: str | None  # Комментарий причины отклонения
    party_id: int  # ID участника
    title: str  # Название компании
    vat: str  # Ставка НДС
    is_vat_included: int  # Включён ли НДС (0/1)
    city: str  # Город
    reason_name: str | None  # Название причины
    delivery_included: str | None  # Включена ли доставка
    comment: str | None  # Общий комментарий


class OfferItem(TypedDict, total=False):
    """
    Описание структуры элемента предложения (offer item) по контракту.
    """

    id: int  # Внутренний ID записи
    offer_id: int  # ID предложения
    item_id: int  # ID позиции (товара/услуги)
    vat: str  # Ставка НДС
    own_currensie: str  # Валюта
    own_currensie_rate: str  # Курс валюты
    price: str  # Цена с НДС (строка, т.к. точность высокая)
    price_no_vat: str  # Цена без НДС (строка)
    price_no_vat_orig: str  # Исходная цена без НДС (строка)
    nprice_orig: str  # Исходная цена с НДС (строка) в валюте предложения
