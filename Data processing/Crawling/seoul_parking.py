# -*- coding:utf-8 -*-

import requests
import json

## 구 출력
def getGu():
    url = "https://parking.seoul.go.kr/SearchParking.do"
    resp = requests.post(url)

    gu_list = resp.json()['list']
    print(gu_list)

    gu_dict = dict(list(map(lambda x: x['result_state'], gu_list)))  # json 객체에서 각각의 구 출력
    # return gu_dict


## 서울특별시 해당 구의 주차장 출력 (source 688라인)
def getParking(gu_code=''):
    url = "https://parking.seoul.go.kr/SearchParkingBy.do"
    resp = requests.post(url, data={

    })
    parking_list = resp.json()['list']

    # 이름, 주소, 경도, 위도 가져오기
    result_list = list()
    for parking in parking_list:
        parking_dict = dict()
        parking_dict[''] = parking['']
        # store_dict['s_name'] = store['s_name']
        result_list.append(parking_dict)

    result_dict = dict()
    result_dict['parking_list'] = result_list

    # json 저장
    result_json = json.dumps(result_dict, ensure_ascii=False)
    with open('starbucks01.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

    return result_json


if __name__ == '__main__' :
    print(getGu())
    print(getParking())
