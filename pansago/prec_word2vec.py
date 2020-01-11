import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
import logging
from gensim.models import word2vec, Word2Vec
from collections import Counter
from preprocessing import preprocessing

def precSaveModel():
    prec = pd.read_csv('./law_list_detail.csv', encoding='utf-8')
    prec = prec.fillna('NA')

    # p = r'.*(특허).*'
    # prec = prec[prec['law_title'].str.match(p) | prec['law_content'].str.match(p)]

    sample_prec_content = prec['law_content'].apply(preprocessing)

    tokenizer = RegexTokenizer()

    token_prec_content = sample_prec_content.apply(tokenizer.tokenize)

    print(token_prec_content, '\n')

    # word2vec 모델 학습에 로그를 찍음
    # logging.basicConfig(
    #     format='%(asctime)s : %(levelname)s : %(message)s',
    #     level=logging.INFO)

    model = word2vec.Word2Vec(token_prec_content, min_count=1, size=500, workers=1)

    # vocab = model.wv.vocab
    # sorted(vocab, key=vocab.get, reverse=True)

    model_name = 'prec_word2vec_model'
    model.save(model_name)

def precUsingModel(keyword):
    model = Word2Vec.load('prec_word2vec_model')

    similar_words = model.wv.most_similar(keyword, topn=5)

    # topn 파라미터로 출력개수 설정가능
    return similar_words