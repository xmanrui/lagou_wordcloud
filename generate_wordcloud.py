
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from get_position_description import get_all_jobs_description
from common import check_contain_chinese, add_words, set_show_Chinese, get_job_type_from_position_info_xlsx
import jieba
from openpyxl import load_workbook
from read_position_info import get_salary_list

set_show_Chinese()
font = './font/SourceHanSerifSC-Regular.otf'

def filter_not_it_job(x):
    flag = not x.isspace() and x.isprintable()
    flag = flag and not x.isnumeric() and not x.isdecimal() and not x.isdigit()
    flag = flag and len(x) > 1

    return flag


def filter_it_job(x):
    if x in add_words:
        return True
    flag = not x.isspace() and x.isprintable()
    flag = flag and not x.isnumeric() and not x.isdecimal() and not x.isdigit()
    flag = flag and len(x) > 1
    flag = flag and (not check_contain_chinese(x))

    return flag


def is_it_job(job_type):
    '''
    包含中文的是非it工作（如产品，运行), it工作指Python、C++、Java等，暂时不考虑HR之类的工作。
    :param job_type:
    :return:
    '''
    flag = check_contain_chinese(job_type)

    return not flag


def filter_fun(job_type):
    '''
    返回it工作或者非it工作的过滤函数
    由于it工作或者非it工作的职位信息分词不一样，it工作的职位信息分词主要是英文如Linux,Git,NoSQL等所以
    过滤方法不一样
    :param job_type:
    :return:
    '''
    if is_it_job(job_type):
        return filter_it_job
    else:
        return filter_not_it_job


def generate_skill_wordcloud(xlsx_file):
    job_type = get_job_type_from_position_info_xlsx(xlsx_file)
    desc = get_all_jobs_description(xlsx_file)
    text = ''.join(desc)
    seg = jieba.cut(text, cut_all=False, HMM=True)
    seg = filter(filter_fun(job_type), seg)
    seg = [s.title() for s in seg]
    text = ' '.join(seg)

    wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2, max_words=1000).generate(text)
    plt.imshow(wc)
    plt.title('%s 技术栈词云图' % job_type, fontsize=20)
    plt.axis("off")
    plt.show()

    wc.to_file('./img_wordcloud/%s_skill_wordcloud.png' % job_type)


def generate_salary_worlcloud(xlsx_file):
    job_type = get_job_type_from_position_info_xlsx(xlsx_file)
    salary_list = get_salary_list(xlsx_file)
    text = ' '.join(salary_list)
    regexp = r"(\w[\w']+| \d+k-\d+k)"

    wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2, max_words=1000, regexp=regexp).generate(text)
    plt.imshow(wc)
    plt.title('%s 工资词云图' % job_type, fontsize=20)
    plt.axis("off")
    plt.show()

    wc.to_file('./img_wordcloud/%s_salary_wordcloud.png' % job_type)

if __name__ == '__main__':
    job = '运营'
    xlsx = './xlsx_file/%s_position_info.xlsx' % job
    print(job)
    #generate_skill_wordcloud(xlsx)
    generate_salary_worlcloud(xlsx)
    print('end!!!', job)
