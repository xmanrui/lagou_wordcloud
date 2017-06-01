
import re
from common import get_job_type_from_position_info_xlsx, set_show_Chinese
from read_position_info import get_salary_list
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

set_show_Chinese()

def calculate_average_salary(xlsx_file):
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

    return job_type, average_lower_limit, average_upper_limit


def plot_average_salary_histogram(job_list):
    job_list = [job.lower() for job in job_list]
    xlsx_list = ['./xlsx_file/%s_position_info.xlsx' % job for job in job_list]
    r = []
    for xlsx in xlsx_list:
        t = calculate_average_salary(xlsx)
        r.append(t)

    r.sort(key=lambda x: x[1])

    jobs = []
    lower_limits = []
    upper_limits = []
    offset_list = []
    for item in r:
        jobs.append(item[0])
        lower_limits.append(item[1])
        upper_limits.append(item[2])
        offset_list.append(item[2] - item[1])

    r_copy = r[:]
    r_copy.sort(key=lambda x: x[2], reverse=True)
    [print('%s: %0.2fk - %0.2fk' % (x[0], x[1], x[2])) for x in sorted(r[:], key=lambda y: y[2], reverse=True)]
    y_max = r_copy[0][2] + 5
    opacity = 0.8
    bar_width = 0.7
    index = np.arange(0, len(r)*2, 2)

    ymajor_locator = MultipleLocator(2)  # 将y轴主刻度标签设置为2的倍数
    # ymajor_formatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
    yminor_locator = MultipleLocator(0.5)  # 将此y轴次刻度标签设置为0.5的倍数
    ax = plt.gca()
    ax.yaxis.set_major_locator(ymajor_locator)
    ax.yaxis.set_minor_locator(yminor_locator)

    # ax.yaxis.set_major_formatter(ymajor_formatter)
    #plt.bar(index, lower_limits, bar_width, alpha=opacity, color='b', label='下限平均值')
    #plt.bar(index + bar_width, upper_limits, bar_width, alpha=opacity, color='r', label='上限平均值')

    plt.bar(index + bar_width/2, offset_list, bar_width, bottom=lower_limits, alpha=opacity, color='r')

    for i, v in enumerate(index):
        lower = '%0.1fk' % r[i][1]
        upper = '%0.1fk' % r[i][2]
        offset = bar_width/5 * 2
        plt.text(v + offset, r[i][1] - 1, lower)
        plt.text(v + offset, r[i][2] + 0.5, upper)

    plt.xlabel('职位')
    plt.ylabel('工资')
    plt.title('工资上下限平均值')
    plt.xticks(index + bar_width, jobs)
    plt.ylim(0, y_max)
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig('./img_wordcloud/salary_histogram.png')

    plt.tight_layout()
    plt.show()


def test_calculate_average_salary():
    job_list1 = ['java', 'python', 'c++', 'c#', 'cocos2d-x', 'unity3d', '安卓', '前端', 'ios', 'opengl']
    # job_list = ['爬虫', '测试', '嵌入式', 'JavaScript', '自然语言处理', '数据挖掘', '机器学习', '大数据', '产品', '需求', '运营']
    # job_list.extend(job_list1)
    plot_average_salary_histogram(job_list1)


if __name__ == '__main__':
    test_calculate_average_salary()


