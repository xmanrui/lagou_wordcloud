
import re
from openpyxl import load_workbook
from common import get_job_type_from_position_info_xlsx
from read_position_info import get_salary_list


def calulate_average_salary(xlsx_file):
    salary_list = get_salary_list(xlsx_file)
    text = ' '.join(salary_list)
    lower_limit = r"(\d+)k-"
    upper_limit = r"-(\d+)k"
    results_lower_limit = re.findall(lower_limit, text)
    results_lower_limit = [int(i) for i in results_lower_limit]
    results_upper_limit = re.findall(upper_limit, text)
    results_upper_limit = [int(i) for i in results_upper_limit]

    average_lower_limit = sum(results_lower_limit) / len(results_lower_limit)
    average_upper_limit = sum(results_upper_limit) / len(results_upper_limit)
    job_type = get_job_type_from_position_info_xlsx(xlsx_file)

    return (average_lower_limit, average_upper_limit)


def test_calulate_average_salary():
    # job_type = 'java'
    # xlsx = './xlsx_file/%s_position_info.xlsx' % job_type
    # calulate_average_salary(xlsx)
    #
    # job_type = 'python'
    # xlsx = './xlsx_file/%s_position_info.xlsx' % job_type
    # calulate_average_salary(xlsx)
    #
    # job_type = 'c++'
    # xlsx = './xlsx_file/%s_position_info.xlsx' % job_type
    # calulate_average_salary(xlsx)

    job_list1 = ['java', 'python', 'c++', 'c#', 'cocos2d-x', 'unity3d', '安卓', '前端', 'ios', 'opengl']
    job_list = ['爬虫', '测试', '嵌入式', 'JavaScript', '自然语言处理', '数据挖掘', '机器学习', '大数据', '产品', '需求', '运营']
    job_list.extend(job_list1)
    r = list()
    for job in job_list:
        xlsx = './xlsx_file/%s_position_info.xlsx' % job.lower()
        job_type = get_job_type_from_position_info_xlsx(xlsx)
        t = calulate_average_salary(xlsx)
        a = [job_type]
        a.extend(t)
        r.append(a)

    r.sort(key=lambda x: x[1], reverse=True)
    print(r)
    for i in r:
        s = '%s: %0.2fk - %0.2fk' % (i[0], i[1], i[2])
        print(s)


if __name__ == '__main__':
    test_calulate_average_salary()


