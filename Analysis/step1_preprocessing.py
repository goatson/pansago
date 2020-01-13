import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
from stopwords import make_stopword
from soynlp.noun import LRNounExtractor
from collections import Counter
import re
from stopwords import make_stopword

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
print(prec['law_jumoon'].iloc[0])
noun_extractor = LRNounExtractor(verbose=True)
noun_extractor.train(preprocessing(prec['law_jumoon'].iloc[0]))
nouns = noun_extractor.extract()
# print(type(nouns))

print(nouns)

