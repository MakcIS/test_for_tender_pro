from random import randint

from openpyxl import Workbook

workbook = Workbook()

ws = workbook.active
row = [randint(1, 500) for _ in range(10)]

ws.append(row)

workbook.save('test.xlsx')
