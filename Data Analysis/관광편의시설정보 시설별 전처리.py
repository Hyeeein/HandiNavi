import pandas as pd
import numpy as np

data = pd.read_csv('서울특별시 장애인 관광편의시설 정보_위도_경도.csv')

print(data.head())
fac = data['시설명']
print(fac.head())


condition1 = (fac.str.contains('우체국|주민센터|구청|회관|공단|국민|경찰|파출|치안|세무서|지구대')) #공공기관
condition2 = fac.str.contains('초등학교|중학교|고등학교|대학교|어린이집|유치원|학원|도서관|청소년|초|증|고') #교육기관
condition3 = fac.str.contains('교회|성당') #종교시설
condition4 = fac.str.contains('마트|시장|백화점|홈플러스|마켓') #마트
condition5 = fac.str.contains('화장실')#화장실
condition6 = fac.str.contains('병원|장례식장|내과|외과|보건|이비인|치과|의원|재활|관절|안과') #의료시설
condition7 = fac.str.contains('은행') #은행
condition8 = fac.str.contains('CGV|시네마|메가박스') #영화관
condition9 = ~(condition1&condition2&condition3&condition4&condition5&condition6&condition7&condition8)




data['시설분류'] = np.nan
data.loc[condition1, '시설분류'] = '공공기관'
data.loc[condition2 , '시설분류'] = '교육기관'
data.loc[condition3 , '시설분류'] = '종교시설'
data.loc[condition4 , '시설분류'] = '마트'
data.loc[condition5 , '시설분류'] = '화장실'
data.loc[condition6 , '시설분류'] = '의료시설'
data.loc[condition7 , '시설분류'] = '은행'
data.loc[condition8 , '시설분류'] = '영화관'
# data[~condition9]='기타'

data.시설분류.replace(to_replace=np.nan, value='기타')

data.to_csv('관광편의시설정보 시설별 분류.csv' , encoding='utf-8-sig')




