import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 텍스트 데이터 전처리
def preprocessing(text):

    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    return text

def substringTags(text):
    result = re.sub('<(/)?([a-zA-Z]*)(-[a-zA-Z]*)?(-[a-zA-Z]*)?(-[a-zA-Z]*)?(\\s[a-zA-Z]*(\\s)?(\\s)?=[^>]*)?(\\s)*(/)?>', '', text)

    return result

def displayWordCloud(data=None, backgroundcolor='white', width=800, height=600):
    stopwords_kr = ['하지만', '그리고', '그런데', '저는', '제가', '그럼', '이런', '저런', '합니다', '많은', '많이', '정말', '너무']

    wordcloud = WordCloud(
                        font_path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf',
                        stopwords = stopwords_kr,
                        background_color = backgroundcolor,
                        width = width,
                        height = height).generate(data)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

tokenizer = RegexTokenizer()

# print(prec['law_content'])

# contents = prec['law_content'].apply(substringTags)

contents = prec['law_content']

tokens = contents.apply(tokenizer.tokenize)

print(tokens[:10])

# displayWordCloud(contents)