import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

font_list = [font.name for font in fm.fontManager.ttflist]
# print(font_list)
plt.rcParams['font.family'] = 'HYGothic-Medium'

data = pd.read_csv('calltaxi_전처리완료.csv' , encoding='utf-8-sig')
# print(data)
data['운행시작'] = pd.to_datetime(data['운행시작'] , errors='coerce') #오류 방지
data = data.set_index('운행시작')

# data = data.set_index('운행시작')
# print(data.index)

# # 시간대별 구분
data['운행시작_시간대별'] = 'N/A'

time01 = data.between_time('01:00:01', '02:00:00')
time02 = data.between_time('02:00:01', '03:00:00')
time03 = data.between_time('03:00:01', '04:00:00')
time04 = data.between_time('04:00:01', '05:00:00')
time05 = data.between_time('05:00:01', '06:00:00')
time06 = data.between_time('06:00:01', '07:00:00')
time07 = data.between_time('07:00:01', '08:00:00')
time08 = data.between_time('08:00:01', '09:00:00')
time09 = data.between_time('09:00:01', '10:00:00')
time10 = data.between_time('10:00:01', '11:00:00')
time11 = data.between_time('11:00:01', '12:00:00')
time12 = data.between_time('12:00:01', '13:00:00')
time13 = data.between_time('13:00:01', '14:00:00')
time14 = data.between_time('14:00:01', '15:00:00')
time15 = data.between_time('15:00:01', '16:00:00')
time16 = data.between_time('16:00:01', '17:00:00')
time17 = data.between_time('17:00:01', '18:00:00')
time18 = data.between_time('18:00:01', '19:00:00')
time19 = data.between_time('19:00:01', '20:00:00')
time20 = data.between_time('20:00:01', '21:00:00')
time21 = data.between_time('21:00:01', '22:00:00')
time22 = data.between_time('22:00:01', '23:00:00')
time23 = data.between_time('23:00:01', '00:00:00')
time24 = data.between_time('00:00:01', '01:00:00')
#
data.loc[time01.index, '운행시작_시간대별'] = '01시'
data.loc[time02.index, '운행시작_시간대별'] = '02시'
data.loc[time03.index, '운행시작_시간대별'] = '03시'
data.loc[time04.index, '운행시작_시간대별'] = '04시'
data.loc[time05.index, '운행시작_시간대별'] = '05시'
data.loc[time06.index, '운행시작_시간대별'] = '06시'
data.loc[time07.index, '운행시작_시간대별'] = '07시'
data.loc[time08.index, '운행시작_시간대별'] = '08시'
data.loc[time09.index, '운행시작_시간대별'] = '09시'
data.loc[time10.index, '운행시작_시간대별'] = '10시'
data.loc[time11.index, '운행시작_시간대별'] = '11시'
data.loc[time12.index, '운행시작_시간대별'] = '12시'
data.loc[time13.index, '운행시작_시간대별'] = '13시'
data.loc[time14.index, '운행시작_시간대별'] = '14시'
data.loc[time15.index, '운행시작_시간대별'] = '15시'
data.loc[time16.index, '운행시작_시간대별'] = '16시'
data.loc[time17.index, '운행시작_시간대별'] = '17시'
data.loc[time18.index, '운행시작_시간대별'] = '18시'
data.loc[time19.index, '운행시작_시간대별'] = '19시'
data.loc[time20.index, '운행시작_시간대별'] = '20시'
data.loc[time21.index, '운행시작_시간대별'] = '21시'
data.loc[time22.index, '운행시작_시간대별'] = '22시'
data.loc[time23.index, '운행시작_시간대별'] = '23시'
data.loc[time24.index, '운행시작_시간대별'] = '24시'

#
# print(data['운행시작_시간대별'].unique())
# print(data['운행시작_시간대별'].nunique())

data_time_counting = data['운행시작_시간대별'].value_counts()
# print(data_time_counting)
data_time_counting_sort = data_time_counting.sort_index()
# print(data_time_counting_sort)

# 라벨링 만들기
labels = []
for i in data_time_counting_sort.index:
    labels.append(i)
print(labels)
# plt.plot(data_time_counting_sort.index , data_time_counting_sort.values)
# plt.show()

# 값(values 설정)
values = data_time_counting_sort.values
label = "콜택시"
plt.figure(figsize=(20,10))
plt.plot(labels, values, marker='s' , color='royalblue' , label=label)
plt.grid(axis='y')
plt.axhline(y= values.mean(), linestyle='--', color='C8', label="평균횟수")
plt.text(21 , values.mean()+100 , f'평균횟수 : {round(values.mean() , )}회')

plt.title("시간대별 장애인 콜택시 이용 현황" , fontsize = 18)
plt.xlabel('시간대별' , fontsize= 16)
plt.ylabel('이용 횟수' , fontsize = 16)
plt.legend()
plt.show()
