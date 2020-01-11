import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
import logging
from gensim.models import word2vec
from collections import Counter

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

prec = pd.read_csv('./law_list_detail.csv', encoding='utf-8')
prec = prec.fillna('NA')

p = r'.*(이혼).*'

prec = prec[prec['law_title'].str.match(p) | prec['law_content'].str.match(p)]

sample_prec_content = prec['law_content'].apply(preprocessing)

tokenizer = RegexTokenizer()

token_prec_content = sample_prec_content.apply(tokenizer.tokenize)

print(token_prec_content, '\n')

# word2vec 모델 학습에 로그를 찍음
# logging.basicConfig(
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     level=logging.INFO)

model = word2vec.Word2Vec(token_prec_content, min_count=10, size=500, workers=1)

model_name = 'prec_word2vec_model'
model.save(model_name)

vocab = model.wv.vocab
print(sorted(vocab, key=vocab.get, reverse=True))