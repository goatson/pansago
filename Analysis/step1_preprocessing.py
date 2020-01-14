import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
from soynlp.tokenizer import RegexTokenizer
from stopwords import make_stopword
from soynlp.noun import LRNounExtractor
from konlpy.tag import *
from collections import Counter
import re
from stopwords_keyword import make_stopword

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

prec = pd.read_csv('C:/Users/admin/Documents/pansago/law_list_detail.csv', encoding='utf-8')

# print(prec.shape)
# print(prec.head())
# print(prec.tail())
# print(prec.info())
# print(prec.isnull().sum())
# print(prec.dtypes)
# print(prec.columns)
# 선고일자에서 앞 4자리를 슬라이스 후 연도 컬럼 생성

law_jumoon = []

for tmp in prec['law_content']:
    try :
        sub1 = tmp.split('문】')[1].split('【')[0]
        law_jumoon.append(sub1)
    except :
        law_jumoon.append('123')


prec['law_jumoon'] = law_jumoon

prec['law_title'].fillna('1', inplace=True)
keyword = input("사건명을 입력하세요 : ")
prec_keyword = prec[prec['law_title'].str.contains(keyword)]['law_jumoon']
print(prec_keyword)
stopwords_keyword = make_stopword()
noun_extractor = LRNounExtractor(verbose=True)
noun_extractor.train(prec_keyword.astype('str').apply(preprocessing))
nouns = noun_extractor.extract()
count = Counter(nouns)
word_list = []
for n, c in count.most_common(1000) :
        if n not in stopwords_keyword :
            dics = {'tag': n, 'count': c[0]}
            word_list.append(dics)
            print(dics)

# for k in prec_keyword :
#     if k not in stopwords_keyword :
#         word_list.append(k)
# print(word_list)        