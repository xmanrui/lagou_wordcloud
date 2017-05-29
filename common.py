import time
import random

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


def random_time_sleep(base_time=20, max_randint=20):
    '''
    随机延时解决访问会被拒绝的问题(如果延时时间固定或者不延时的话会被禁止访问）
    todo: 具体延时在多少范围合适，还没有经过精准测试
    :param base_time:
    :return:
    '''
    sleep_sec = base_time + random.randint(0, max_randint)
    time.sleep(sleep_sec)
