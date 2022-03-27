import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

font_list = [font.name for font in fm.fontManager.ttflist]
# print(font_list)
plt.rcParams['font.family'] = 'HYGothic-Medium'

data = pd.read_csv('calltaxi_전처리완료.csv')
# print(data.head())

# 아침
morning = data[data['구분']=='아침']
morning_day = morning['요일'].value_counts()
morning_dayday = morning_day.reindex(['월요일' , '화요일' , '수요일' , '목요일' , '금요일' , '토요일' , '일요일']) # 순서대로 reindex
morning_values = morning_dayday.values

# 점심
afternoon = data[data['구분']=='점심']
afternoon_day = afternoon['요일'].value_counts()
afternoon_dayday = afternoon_day.reindex(['월요일' , '화요일' , '수요일' , '목요일' , '금요일' , '토요일' , '일요일']) # 순서대로 reindex
afternoon_values = afternoon_dayday.values

#저녁
evening = data[data['구분']=='저녁']
evening_day = evening['요일'].value_counts()
evening_dayday = evening_day.reindex(['월요일' , '화요일' , '수요일' , '목요일' , '금요일' , '토요일' , '일요일']) # 순서대로 reindex
evening_values = evening_dayday.values

#심야
midnight = data[data['구분']=='심야']
midnight_day = midnight['요일'].value_counts()
midnight_dayday = midnight_day.reindex(['월요일' , '화요일' , '수요일' , '목요일' , '금요일' , '토요일' , '일요일']) # 순서대로 reindex
midnight_values = midnight_dayday.values

labels = []
for i in morning_dayday.index:
    labels.append(i)



plt.figure(figsize=(16,12))
plt.title('요일별 운행횟수', fontsize=20)
plt.ylabel('운행 횟수', fontsize=18)
plt.xlabel('요일', fontsize=18)
p_morning = plt.bar(labels, morning_values, color='C0',  label='아침(6시~12시' , alpha=0.7)
p_afternoon = plt.bar(labels, afternoon_values, color='C0' ,  label='점심(12시~18시)' , alpha=0.5,
                      bottom=morning_values)
p_evening = plt.bar(labels, evening_values, color = 'C0' ,  label = '저녁(18시~24시)' ,alpha=0.3,
                    bottom=afternoon_values+morning_values)
p_midnight = plt.bar(labels, midnight_values , color = 'C0' ,  label = '심야(24시~6시)', alpha=0.1,
                     bottom=morning_values+afternoon_values+evening_values)
plt.text(-0.05, 2000 , '39%' , fontsize=10) #월/아침
plt.text(0.95, 2000 , '41%' , fontsize=10) # 화/아침
plt.text(1.95, 2000 , '42%' , fontsize=10) # 수/아침
plt.text(2.95, 2000 , '42%' , fontsize=10) #목/아침
plt.text(3.95, 2000 , '42%' , fontsize=10) #금/아침
plt.text(4.95, 1400 , '43%' , fontsize=10) #토/아침
plt.text(5.95, 1000 , '39%' , fontsize=10) #일/아침

plt.text(-0.05, 6200 , '45%' , fontsize=10) #월/점심
plt.text(0.95, 6200 , '45%' , fontsize=10) #화/점심
plt.text(1.95, 6100 , '44%' , fontsize=10) #수/점심
plt.text(2.95, 6150 , '44%' , fontsize=10) #목/점심
plt.text(3.95, 6200 , '44%' , fontsize=10) #금/점심
plt.text(4.95, 3900 , '40%' , fontsize=10) #토/점심
plt.text(5.95, 3400 , '45%' , fontsize=10) #일/점심

plt.text(-0.05, 9300 , '13%' , fontsize=10) #월/저녁
plt.text(0.95, 9050 , '12%' , fontsize=10) #화/저녁
plt.text(1.95, 8700 , '11%' , fontsize=10) #수/저녁
plt.text(2.95, 8900 , '12%' , fontsize=10) #목/저녁
plt.text(3.95, 9000 , '11%' , fontsize=10) #금/저녁
plt.text(4.95, 5600 , '14%' , fontsize=10) #토/저녁
plt.text(5.95, 5300 , '15%' , fontsize=10) #일/저녁

# plt.text(0, 1050 , f'평균횟수 ff:회')
plt.legend()
plt.show()




