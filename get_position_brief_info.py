import requests
from openpyxl import Workbook
from pprint import pprint
import time
import random
from urllib.parse import quote


headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept-Encoding': 'gzip, deflate',
           'Host': 'www.lagou.com',
           'Origin': 'http://www.lagou.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://www.lagou.com',
           'Proxy-Connection': 'keep-alive',
           'X-Anit-Forge-Code': '0',
           'X-Anit-Forge-Token': None}

cookies = {
'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1496037147',
'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1495978029,1496037031',
'JSESSIONID': 'ABAAABAACEBACDG2BBDDB61224154CEB66EB746B9D3D335',
'LGRID': '20170529135330-24d072fb-4433-11e7-943b-5254005c3644',
'LGSID': '20170529135135-e003dae5-4432-11e7-b8a4-525400f775ce',
'LGUID': '20160330235031-21c49d21-f68f-11e5-bab4-5254005c3644',
'PRE_HOST': '',
'PRE_LAND': '',
'PRE_SITE': '',
'PRE_UTM': '',
'SEARCH_ID': '7f77002a2d1f4472905cfae70eead634',
'TG-TRACK-CODE': 'index_search',
'_ga': 'GA1.2.254567398.1459353026',
'_gid': 'GA1.2.808713108.1496037147',
'index_location_city': '%E6%B7%B1%E5%9C%B3',
'tencentSig': '6106549248',
'user_trace_token': '2016033023503'
}


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
        info.append(i['companySize'])
        info.append(i['positionId'])
        info_list.append(info)
    return info_list


def main(city_name, lang_name):
    lang_name = lang_name.lower()
    page = 1
    # url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    city_quote = quote(city_name)
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&city=%s' % city_quote
    info_result = []
    while page < 2:
        info = get_json(url, page, lang_name)
        info_result += info
        page += 1
        # 如果暂停的时间一样会被拒绝访问， 所以修改为随机值，每次都不一样绕开反爬虫策略
        time.sleep(20 + random.randint(0, 20))
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name
    for row in info_result:
        ws1.append(row)
    wb.save('./xlsx_file/%s_position_info.xlsx' % lang_name)


if __name__ == '__main__':
    lang = 'python'
    city = '深圳'
    main(city, lang)
    print('end')
