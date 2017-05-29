# -*- coding-8 -*-
from openpyxl import load_workbook
import os


def get_company_id(xlsx_file):
    basename = os.path.basename(xlsx_file)
    str_split = basename.split('_')
    lang_name = str_split[0]
    wb = load_workbook(xlsx_file)
    ws = wb.get_sheet_by_name(lang_name)
    rows = len(list(ws.rows))
    list_id = [ws['L%s' % i].value for i in range(1, rows+1)]

    return list_id


def test_get_company_id():
    test_file = './xlsx_file/python_position_info.xlsx'
    a = get_company_id(test_file)
    print(a)

if __name__ == '__main__':
    test_get_company_id()
