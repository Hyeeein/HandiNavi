import pandas as pd
import folium
df1 = pd.read_csv('구별 장애인 수.csv', index_col = '자치구', encoding='utf-8-sig')

df1 = df1.iloc[2:,[1]]
df1.index.name = '구'
df1 = df1.iloc[1:]
df1.sort_index(ascending=True, inplace=True)

df = pd.read_csv('lift.csv', encoding='utf-8-sig')
df = df.dropna(how='all')
df = df.dropna(how='all', axis=1)
df['에스컬레이터 개수'] = df['에스컬레이터 개수'].astype('int')
df['휠체어리프트 개수'] = df['휠체어리프트 개수'].astype('int')
df['전동휠체어 급속충전기 개수'] = df['전동휠체어 급속충전기 개수'].astype('int')
df['승강기 개수'] = df['승강기 개수'].astype('int')
group_df = df.groupby(df['구'])
total_df = group_df.sum()
del total_df['경도']
total_df.sort_index(ascending=True,inplace=True)
total_df['총합'] = total_df['승강기 개수']+total_df['에스컬레이터 개수']+total_df['휠체어리프트 개수']+total_df['전동휠체어 급속충전기 개수']

total = pd.concat([df1, total_df], axis=1)

for i, row in enumerate(total['합계']):
    total['합계'][i] = row.replace(',', '')

total['합계'] = total['합계'].astype('int')
total['비율'] = total['합계']/total['총합']
total['비율']

import matplotlib.pyplot as plt
from importlib import reload
reload(plt)

from matplotlib import font_manager, rc
import sys

if sys.platform in ['win32', 'win64'] :
    font_name = 'malgun gothic'
elif sys.platform == 'darwin' :
    font_name = "AppleGothic"

rc('font', family = font_name)

y = total['비율'].sort_values()
plt.figure(figsize=(10,7))
plt.title('편의시설 1개가 소화해야하는 장애인의 수')
plt.barh(total.index, y, color='#0066cc', alpha=0.5)
plt.axvline(x=total['비율'].mean(), ymin=0.1, ymax=0.9, color='r', linestyle='--', linewidth=2)
plt.text(270,10, '서울시 전체 평균: 약 241명')

plt.show()