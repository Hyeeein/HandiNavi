import pandas as pd
import googlemaps
import numpy as np

data = pd.read_csv('서울특별시 장애인 관광편의시설 정보.csv' , encoding='cp949')

address = data['주소']
googlemaps_key = "AIzaSyDUcaVK-cevl3m70wFhRowUa5SgANfXxmM"
gmaps = googlemaps.Client(key=googlemaps_key)


lst=[]

for i in range(len(address)):
    a = address[i].split(' ')
    b = " ".join(a[0:4])
    lst.append(b)

lat = list()
lng = list()
for i, location in enumerate(lst):
    try:
        geo_location = gmaps.geocode(location)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        print(f"{i}번째 {(data.iloc[i, 3])}의 좌표를 찾을 수 없음")
        lat.append(np.nan)
        lng.append(np.nan)


data['위도']=lat
data['경도']=lng
print(data.head())
data.to_csv('서울특별시 장애인 관광편의시설 정보_위도_경도.csv' ,encoding='utf-8-sig')