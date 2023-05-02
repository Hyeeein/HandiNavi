# -*- coding:utf-8 -*-

import requests
import json

url = "http://parking.seoul.go.kr/SearchParkingBy.do"

gu_list = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구",
           "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구",
           "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
def siDo():
    total_list = []
    for i in gu_list:
        p_list = []
        res = requests.post(url, data={"Gu": i,
                                    "Dong": "전체",
                                    "Keyword": ""})
        datas = res.json()['res_value']['parking_list']
        for data in datas:
            dic = {}
            dic['name'] = data['parking_name']
            dic['capacity'] = data['capacity']
            dic['addr'] = data['address']
            dic['lng'] = data['position_list'][0]['lng']
            dic['lat'] = data['position_list'][0]['lat']
            dic['add_rates'] = data['add_rates']
            dic['rates'] = data['rates']

            p_list.append(dic)

        total_list.append(p_list)
    total_dic = {"total":total_list}

    result_json = json.dumps(total_dic, ensure_ascii=False)

    with open('seoulparking.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

siDo()




