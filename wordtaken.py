import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
# from plotnine import *
import plotnine
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import re
import gensim
import matplotlib as mpl
df = pd.read_csv('./law_list_detail.csv', parse_dates=['law_no', 'law_event_no'])
# df.describe()
# df.describe(include=np.object)
# 그래프에서 한글표현을 위해 폰트를 설치합니다.
# %config InlineBackend.figure_format = 'retina'

fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)

# !apt -qq -y install fonts-nanum
mpl.font_manager._rebuild()
mpl.pyplot.rc('font', family='NanumBarunGothic')

p = r'.*(법원|판결|선고|이혼|강도|절도).*'
finance = df[df['law_title'].str.match(p) |
          df['law_content'].str.match(p, flags=re.MULTILINE)]

# finance.shape
# print(finance.head())
# print(finance.tail())

# def preprocessing(text):
#     #개행문자 제거
    
#     text = re.sub('\\\\n', ' ', text)
    
    
#     text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
#     return text


# sample_index = 10000



# sample_content = finance
# sample_content = preprocessing(sample_content)
# print(sample_content[:100])

