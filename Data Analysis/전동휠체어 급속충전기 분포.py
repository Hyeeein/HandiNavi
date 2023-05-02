import pandas as pd
import folium
df = pd.read_csv('lift.csv', encoding='utf-8-sig')
df = df.dropna(how='all')
df = df.dropna(how='all', axis=1)
df['에스컬레이터 개수'] = df['에스컬레이터 개수'].astype('int')
df['휠체어리프트 개수'] = df['휠체어리프트 개수'].astype('int')
df['전동휠체어 급속충전기 개수'] = df['전동휠체어 급속충전기 개수'].astype('int')
df['승강기 개수'] = df['승강기 개수'].astype('int')
df= df.iloc[:, [0,2,3,4,5]]

group_df = df.groupby(df['구'])
total_df = group_df.sum()
total_df

state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'

m = folium.Map(location=[37.562225, 126.978555], tiles="OpenStreetMap", zoom_start=11)

folium.Choropleth(
    geo_data = state_geo,
    name = '전동휠체어 급속충전기 개수',
    data = total_df['전동휠체어 급속충전기 개수'],
    columns = [df.index, df['전동휠체어 급속충전기 개수']],
    key_on = 'feature.properties.name',
    fill_color = "PuBu",
    fill_opacity=0.7,
    line_opacity=0.3,
    bins = [0,5,10,15,20,25],
    color='gray',
).add_to(m)
m.save('wheelchaircharger_count.html')