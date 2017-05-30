import requests
from openpyxl import Workbook
from pprint import pprint
import time
import random
from urllib.parse import quote
from common import headers, cookies


def get_json(url, page_number, lang_name):
    data = {'first': 'true', 'pn': page_number, 'kd': lang_name}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    proxies = {'http': 'http://222.169.193.162:8099'}

    json = requests.post(url, data, proxies=proxies, headers=headers, cookies=cookies).json()
    list_companies = json['content']['positionResult']['result']
    pprint(list_companies)
    info_list = []
    for i in list_companies:
        info = list()
        info.append(i['companyShortName'])
        info.append(i['positionName'])
        info.append(i['city'])
        info.append(i['industryField'])
        info.append(i['salary'])
        info.append(i['education'])
        info.append(i['workYear'])
        info.append(i['companySize'])
        info.append(i['district'])
        info.append(i['financeStage'])
        info.append(i['businessZones'])
        info.append(i['positionId'])
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
        time.sleep(20 + random.randint(0, 20))
    wb = Workbook()
    ws1 = wb.active
    ws1.title = job_type
    for row in info_result:
        ws1.append(row)
    wb.save('./xlsx_file/%s_position_info.xlsx' % job_type)


if __name__ == '__main__':
    job = '运营'
    city = '深圳'
    main(city, job)
    print('end')
