import warnings
warnings.filterwarnings('ignore')

from pandas import DataFrame as df
import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from collections import Counter
from wordcloud import WordCloud
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from stopwords import make_stopword

# 마이너스 폰트 깨짐 현상 수정
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf'
font_name = fm.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

# 텍스트 데이터 전처리
def preprocessing(text):

    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)

    # 【피 고 인】형식 문자 제거
    text = re.sub(r'\【[^)]*\】', '', text)

    # 양 끝 공백 제거
    text = text.strip()

    # 문자 중간 공백 1개
    text = ' '.join(text.split())

    return text

def tag_counting(law_event_type):
    prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

    noun_extractor = LRNounExtractor(verbose=True)
    noun_extractor.train(prec[prec['law_event_type'] == law_event_type]['law_content'].astype('str').apply(preprocessing))
    nouns = noun_extractor.extract()

    count = Counter(nouns)
    print(count)

    tag_count = []
    stopwords = ['것으로', '이하', '또는', '있다', '소외', '없다', '관한', '같은', '소외', '대한', '피고', '원고', '사건', '아니', '사실', '같이', '경우', '이유', '사건본인', '주장', '판결', '대하여', '관하여']

    for n, c in count.most_common(100):
        if n not in stopwords:
            dics = {'tag': n, 'count': c[0]}
            tag_count.append(dics)

        if len(tag_count) == 20:
            break

    for tag in tag_count:
        print("{:<14}".format(tag['tag']), end='\t')
        print("{}".format(tag['count']))

tag_counting('가사')
# tag_counting('민사')
# tag_counting('세무')
# tag_counting('일반행정')
# tag_counting('특허')
# tag_counting('형사')