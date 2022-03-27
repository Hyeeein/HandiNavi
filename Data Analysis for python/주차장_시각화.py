import pandas as pd
import matplotlib.font_manager as fm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import plotly.express as px

font_list = [font.name for font in fm.fontManager.ttflist]

plt.rcParams['font.family'] = 'HYGothic-Medium'

data = pd.read_csv('(final_장애인주차가능여부)seoulparking.csv')
public = data['세부분류'] == '공영주차장'
data_public = data[public]
# print(data_public.columns)
# print(data_public)
# data_public = data_public.drop(columns=['시설명'])
data_public = data_public.drop(columns=['주차가능면'])
data_public = data_public.drop(columns=['시설분류'])
data_public = data_public.drop(columns=['세부분류'])
data_public = data_public.drop(columns=['주소'])
data_public = data_public.drop(columns=['위도'])
data_public = data_public.drop(columns=['경도'])
# print(data_public)

data_group = data_public.groupby(['담당구' , '장애인 주차칸 여부'] , as_index=False).count()
# print(data_group)
# print(type(data_group))
# print(data_group.values)

#
# # print(data_group.values[0][0])
gu = [] #지역구
# print(len(data_group.values))
for i in range(0, len(data_group.values), 2):
    gu.append(data_group.values[i][0])
#
# possible = [] #장애인 주차 가능
# for i in range(0, len(data_group.values), 2):
#     possible.append(data_group.values[i][2])
# # print(possible)
#
# impossible = [] #장애인 주차 불가능
# for i in range(1, len(data_group.values), 2):
#     impossible.append(data_group.values[i][2])
# # print(impossible)
#
# df = pd.DataFrame()
# df['담당구'] = gu
# df['장애인 주차 가능'] = possible
# df['장애인 주차 불가능'] = impossible
# df['합계'] = df['장애인 주차 가능'].values + df['장애인 주차 불가능'].values
# print(df)




# fig = px.treemap(data_group,
#                  path=['담당구' , '장애인 주차칸 여부'  ],
#                  values = '시설명'
#                  )
#
# fig.update_layout(title="주차",
#                   width=1000, height=700,)
#
# fig.show()



data_group.rename(columns={'시설명':'주차장 수'} , inplace= True)
data_group['장애인 주차칸 여부'] = data_group['장애인 주차칸 여부'].replace('가능' , '주차 가능')
data_group['장애인 주차칸 여부'] = data_group['장애인 주차칸 여부'].replace('불가능' , '주차 불가능')

print(data_group)
print(data_group.values)

value = data_group.values.copy()
data_group['장애인 주차칸 비율(%)']=""
ratio = data_group['장애인 주차칸 비율(%)'].copy()

for i in range(len(value)):
    if i == 0:
        ratio[i] = round(value[i][2]/(value[i][2]+value[i+1][2]),2)*100
    elif i%2 ==0:
        ratio[i] = round(
            value[i][2] / (value[i][2] + value[i + 1][2]), 2) * 100

    elif i%2 == 1:
        ratio[i] = round(
            value[i][2] / (value[i][2] + value[i - 1][2]), 2) * 100

data_group['장애인 주차칸 비율(%)'] = ratio
print(data_group)
data_group['장애인 주차칸 비율(%)'] = data_group['장애인 주차칸 비율(%)'].astype(int)
print(data_group)
# print(round(data_group.values[0][2]/(data_group.values[0][2]+data_group.values[1][2])))
# print(data_group.values[0][2])
# print(data_group.values[1][2])
# print(round((data_group.values[0][2] / (data_group.values[0][2]+data_group.values[1][2])) , 2))

fig = px.treemap(data_group,
                 path=['담당구', '장애인 주차칸 여부'],
                 values='주차장 수',
                 color='장애인 주차칸 비율(%)',
color_continuous_scale='RdBu'



                  )

fig.update_layout(title="각 구별 공영 주차장 수/장애인 주차칸 여부",
                margin = dict(t=50, l=25, r=25, b=25),
                  width=1000, height=600,)

fig.show()








# fig = px.treemap(df,
#                  path=['담당구' , '합계', '장애인 주차 가능'  ],
#                  values = '합계'
#                  )
# 
# fig.update_layout(title="주차",
#                   width=1000, height=700,)
# 
# fig.show()