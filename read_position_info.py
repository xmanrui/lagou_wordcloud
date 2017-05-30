# -*- coding-8 -*-
from openpyxl import load_workbook
import os
from common import get_job_type_from_position_info_xlsx


def get_company_ids(xlsx_file):
    job_type = get_job_type_from_position_info_xlsx(xlsx_file)
    wb = load_workbook(xlsx_file)
    ws = wb.get_sheet_by_name(job_type)
    rows = len(list(ws.rows))
    list_id = [ws['L%s' % i].value for i in range(1, rows+1)]

    return list_id


def get_salary_list(xlsx_file):
    job_type = get_job_type_from_position_info_xlsx(xlsx_file)
    wb = load_workbook(xlsx_file)
    ws = wb.get_sheet_by_name(job_type)
    rows = len(list(ws.rows))
    salary_list = [ws['E%s' % i].value for i in range(1, rows+1)]
    return salary_list


def test_get_company_id():
    test_file = './xlsx_file/python_position_info.xlsx'
    a = get_company_ids(test_file)
    print(a)

if __name__ == '__main__':
    test_get_company_id()
