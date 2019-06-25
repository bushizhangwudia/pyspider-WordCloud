# -*- coding: utf-8 -*-
# author zhangwudi
# time 2019-6-25 14:23:47

import time
from wordcloud import WordCloud
import cv2
import jieba


with open('libai.txt', 'r',encoding="utf-8") as f:
    text = f.read()

cut_text = " ".join(jieba.cut(text))

color_mask = cv2.imread('libai.jpg')

cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path=" C:\\Windows\\Fonts\\simkai.ttf",
    # font_path=path.join(d,'simsun.ttc'),
    # 设置背景色
    background_color='white',
    # 词云形状
    mask=color_mask,
    # 允许最大词汇
    max_words=500,
    # 最大号字体
    max_font_size=40
)
wCloud = cloud.generate(cut_text)

now = int(time.time())
timeStruct = time.localtime(now)
strTime = time.strftime("%Y%m%d%H%M%S", timeStruct)

wCloud.to_file(strTime+".jpg")

import matplotlib.pyplot as plt

plt.imshow(wCloud, interpolation='bilinear')
plt.axis('off')
plt.show()