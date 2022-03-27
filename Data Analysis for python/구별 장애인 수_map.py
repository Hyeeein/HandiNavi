import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
df1 = pd.read_csv('구별 장애인 수.csv', encoding='utf-8-sig')

df1 = df1.loc[3:,['자치구', '합계']]

df1.reset_index(drop=True, inplace=True)

for i, data in enumerate(df1['합계']):
    df1['합계'][i] = data.replace(',', '')

df1['합계'] = df1['합계'].astype('int')

df1.index = df1['자치구']
del df1['자치구']
df1
m = folium.Map(location=[37.562225, 126.978555], tiles="OpenStreetMap", zoom_start=11)

state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'

folium.Choropleth(
    geo_data = state_geo,
    data = df1['합계'],
    key_on = 'feature.properties.name',
    fill_color = 'BuPu',
    # fill_opacity=0.7,
    # line_opacity=0.3,
    bins = [5000,10000,15000,20000,25000,30000],
).add_to(m)
m.save('disabled_count.html')