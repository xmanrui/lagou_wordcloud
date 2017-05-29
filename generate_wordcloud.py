
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from get_position_description import get_all_jobs_description
from common import check_contain_chinese, add_words, set_show_Chinese
import jieba

set_show_Chinese()


def filter_fun(x):
    if x in add_words:
        return True

    flag = not x.isdigit() and len(x) > 1 and x.isprintable()
    flag = flag and (not check_contain_chinese(x))

    return flag


def generate_skill_wordcloud(xlsx_file):
    desc = get_all_jobs_description(xlsx_file)
    text = ''.join(desc)
    seg = jieba.cut(text, cut_all=False, HMM=True)
    seg = filter(filter_fun, seg)
    seg = [s.title() for s in seg]
    text = ' '.join(seg)

    font = './font/SourceHanSerifSC-Regular.otf'
    wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2, max_words=1000).generate(text)
    plt.imshow(wc)
    plt.title('Python技术栈词云图', fontsize=20)
    plt.axis("off")
    plt.show()

    wc.to_file('skill_wordcloud.png')

if __name__ == '__main__':
    xlsx = './xlsx_file/python_position_info.xlsx'
    generate_skill_wordcloud(xlsx)
