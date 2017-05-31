import time
import random
import os

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


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def set_show_Chinese():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def get_job_type_from_position_info_xlsx(xlsx_file):
    str_split = os.path.basename(xlsx_file).split('_')
    job_type = str_split[0]
    return job_type

add_words = ['数据库', '分布式', '设计模式', '面向对象', '网络编程', '算法', '数据结构',
        '正则表达式', '敏捷', '单元测试', '并发', '微服务', '集群', '机器学习', 'C++', 'C#', '高性能', '高并发',
        '后台', '前端', '运维', '消息队列', '数据分析', '数据挖掘', '游戏', '大数据', '云计算', '中间件']

stop_words = ['CTO', 'CEO']

no_title_words = ['DBA', 'uWsgi', 'MQ', 'PHP']
