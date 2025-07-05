from openpyxl import Workbook

workbook = Workbook()

ws = workbook.active
ws['A1'] = 5

workbook.save('test.xlsx')