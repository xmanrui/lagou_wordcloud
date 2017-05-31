import requests
from openpyxl import Workbook
from pprint import pprint
import time
import random
from urllib.parse import quote
from common import headers, cookies, random_time_sleep


def list_info_convert_str(info):
    if isinstance(info, list):
        str_info = ' '.join(info)
        return str_info

    return info


def get_json(url, page_number, lang_name):
    data = {'first': 'true', 'pn': page_number, 'kd': lang_name}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    proxies = {'http': 'http://222.169.193.162:8099'}

    json = requests.post(url, data, proxies=proxies, headers=headers, cookies=cookies).json()
    pprint(json)
    list_companies = json['content']['positionResult']['result']
    pprint(list_companies)
    info_list = []
    for i in list_companies:
        info = list()
        info.append(list_info_convert_str(i['companyShortName']))
        info.append(list_info_convert_str(i['positionName']))
        info.append(list_info_convert_str(i['city']))
        info.append(list_info_convert_str(i['industryField']))
        info.append(list_info_convert_str(i['salary']))
        info.append(list_info_convert_str(i['education']))
        info.append(list_info_convert_str(i['workYear']))
        info.append(list_info_convert_str(i['companySize']))
        info.append(list_info_convert_str(i['district']))
        info.append(list_info_convert_str(i['financeStage']))
        info.append(list_info_convert_str(i['businessZones']))
        info.append(list_info_convert_str(i['positionId']))
        info_list.append(info)
    return info_list


def main(city_name, job_type):
    job_type = job_type.lower()
    page = 1
    # url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    city_quote = quote(city_name)
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&city=%s' % city_quote
    info_result = []
    while page < 10:
        info = get_json(url, page, job_type)
        info_result += info
        page += 1
        # 如果暂停的时间一样会被拒绝访问， 所以修改为随机值，每次都不一样绕开反爬虫策略
        random_time_sleep(20, 20)
    wb = Workbook()
    ws1 = wb.active
    ws1.title = job_type
    for row in info_result:
        ws1.append(row)
    wb.save('./xlsx_file/%s_position_info.xlsx' % job_type)


if __name__ == '__main__':
    job = 'python'
    city = '深圳'
    main(city, job)
    print('end')
