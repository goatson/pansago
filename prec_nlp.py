import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stopwords import make_stopword
from preprocessing import preprocessing

def displayWordCloud(data=None, backgroundcolor='white', width=800, height=600):
    stopwords_kr = make_stopword()
    print('불용어 리스트 : ', stopwords_kr)

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

contents = prec['law_content'].astype('str').apply(preprocessing)
print(contents)

displayWordCloud(' '.join(contents))