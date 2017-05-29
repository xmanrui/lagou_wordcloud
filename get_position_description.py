

import requests
from common import headers, random_time_sleep
from bs4 import BeautifulSoup
from read_position_info import get_company_ids
import os


def get_job_description(company_id):
    job_url = 'https://www.lagou.com/jobs/%s.html' % str(company_id)
    response = requests.get(job_url, headers=headers, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html5lib')
        doms = soup.find_all('dd', class_='job_bt')[0]
        doms = doms.find_all('div')[0]
        doms = doms.find_all('p')
        return [item.get_text() for item in doms]
        # for item in doms:
        #     yield item.get_text()
    elif response.status_code == 403:
        print('request is forbidden by the server...')
    else:
        print(response.status_code)


def get_all_jobs_description(xlsx_file):
    list_id = get_company_ids(xlsx_file)
    info = []
    for _id in list_id:
        desc = get_job_description(_id)
        if desc:
            info.extend(desc)
        random_time_sleep(3, 7)

    return info


if __name__ == '__main__':
    d = os.path.dirname(__file__)
    xlsx = os.path.join(d, 'xlsx_file/python_position_info.xlsx')
    r = get_all_jobs_description(xlsx)
    print(r)
