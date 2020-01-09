from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import numpy as np

mask = np.array(Image.open('./pansago/static/src/hoocloud.png'))

#텍스트를 읽어주시면 됩니다.
text = open('./law_list_detail.csv').read()

# 그리고 다음과 같이 WordCloud 객체를 만들어 주시고
wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', background_color="white", max_words=500, mask=mask,max_font_size=300)
#텍스트를 읽어주시면 됩니다.

wordcloud = WordCloud(max_font_size=100).generate(text)


# 다음과 같이 파일로 저장해주시면 끝이 납니다~!
wc.to_file('goodword.png')

# 이와 같이 그냥 한글폰트만 찾아주셔서 경로만 써주면 돼요~~




# Display the generated image:
# the matplotlib way:

# fig = plt.figure()
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.savefig('./pansago/static/src/wordbeauty.svg')