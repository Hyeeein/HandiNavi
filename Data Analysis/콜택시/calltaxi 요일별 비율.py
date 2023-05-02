import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

font_list = [font.name for font in fm.fontManager.ttflist]
# print(font_list)
plt.rcParams['font.family'] = 'HYGothic-Medium'

data = pd.read_csv('calltaxi_전처리완료.csv')

#월요일
monday = data[data['요일']=='월요일']
monday_day = monday['구분'].value_counts(normalize=True)
# print(round(monday_day*100))
#점심    45.0
# 아침    39.0
# 저녁    13.0
# 심야     3.0

tuesday = data[data['요일']=='화요일']
tuesday_day = tuesday['구분'].value_counts(normalize=True)
# print(round(tuesday_day*100))
# 점심    45.0
# 아침    41.0
# 저녁    12.0
# 심야     2.0

wday = data[data['요일']=='수요일']
wday_day = wday['구분'].value_counts(normalize=True)
# print(round(wday_day*100))
# 점심    44.0
# 아침    42.0
# 저녁    11.0
# 심야     2.0

thursday = data[data['요일']=='목요일']
thursday_day = thursday['구분'].value_counts(normalize=True)
# print(round(thursday_day*100))
# 점심    44.0
# 아침    42.0
# 저녁    12.0
# 심야     2.0

friday = data[data['요일']=='금요일']
friday_day = friday['구분'].value_counts(normalize=True)
# print(round(friday_day*100))
# 점심    44.0
# 아침    42.0
# 저녁    11.0
# 심야     3.0

saturday = data[data['요일']=='토요일']
saturday_day = saturday['구분'].value_counts(normalize=True)
print(round(saturday_day*100))
# 아침    43.0
# 점심    40.0
# 저녁    14.0
# 심야     4.0

sunday = data[data['요일']=='일요일']
sunday_day = sunday['구분'].value_counts(normalize=True)
print(round(sunday_day*100))
# 점심    45.0
# 아침    36.0
# 저녁    15.0
# 심야     4.0