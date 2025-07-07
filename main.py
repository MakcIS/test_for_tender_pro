from domain.mappers.offer import OfferItemMapper, OfferMapper
from domain.mappers.tender import TenderMapper
from reports.excel_service import ExcleWorkbookCreaterService
from reports.prepare import DataPreparer
from test_data import get_test_data


def main():
    offers, tenders, offer_items = get_test_data()
    offers = OfferMapper.list_dto_to_entity(offers)
    offer_items = OfferItemMapper.list_dto_to_dict(offer_items)
    tenders = TenderMapper.list_dto_to_entity(tenders)
    data = DataPreparer(offers, offer_items, tenders).get_data()
    workbook = ExcleWorkbookCreaterService(data).workbook_creater()
    workbook.save("report.xlsx")


if __name__ == "__main__":
    main()
