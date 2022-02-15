# -*- coding:utf-8 -*-

import requests
import json

### 시도 출력
def getSido():
    # 여기서 endpoint(서버 root)는 https://www.starbucks.co.kr/
    # service_url은 store/getSidoList, 뒤에 .do는 신경쓰지 말기 (그냥 붙이는 것)
    # 1261줄 : __ajaxCall("/store/getSidoList.do", {}, true, "json", "post", ...
    url = "https://www.starbucks.co.kr/store/getSidoList.do"

    resp = requests.post(url)
    # print(resp)         # 결과가 response[200]으로 출력되면 성공했다, 잘 응답받았다를 의미
    # print(resp.json())  # resp.text는 응답받은 '문자열'이므로 resp.json하여 바로 json 형태로 바꿔줌

    # 여기서 우리가 원하는건 sido_cd:'01', sido_nm:'서울' 출력

    # 1) 객체 안에 리스트 값으로 들어가 있으므로 아래 코드 실행하면 'list'부분의 배열이 출력 => json 객체로 출력
    sido_list = resp.json()['list']

    # 2) json 객체에서 각각의 시도 출력
    sido_code = list(map(lambda x: x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x:x['sido_nm'], sido_list))
    # print(sido_code)
    # print(sido_nm)

    # 3) list 2개를 한 번에 묶어줄 수 있음 (zip)
    sido_dict = dict(zip(sido_code, sido_nm))
    return sido_dict


### 구군 출력
def getGuGun(sido_code):
    # 1302줄 : __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={'sido_cd': sido_code})

    # 응답 받은 것 중에 list에 해당하는 것을 불러오기
    gugun_list = resp.json()['list']
    # print(gugun_list)

    # 구군 데이터를 받아옴
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_list)),
                          list(map(lambda x: x['gugun_nm'], gugun_list))))
    return gugun_dict


## 어떤 시의 매장, 어떤 시의 '어떤 군'의 매장
def getStore(sido_code='', gugun_code=''):
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post", ...
    url = "https://www.starbucks.co.kr/store/getStore.do"
    resp = requests.post(url, data={'ins_lat': '37.3844693',
                                    'ins_lng': '126.7846436',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date': ''})
    store_list = resp.json()['list']

    # s_name, tel, doro_address, lat, lot을 전체 리스트로 가져올 수 있음

    result_list = list() # 저장할 내용 담는 리스트
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    # {'store_list':[{}, {}, {}]} 형태로 만들 수 있음
    result_dict = dict()
    result_dict['store_list'] = result_list

    # json 저장
    result_json = json.dumps(result_dict, ensure_ascii=False)
    with open('starbucks01.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

    return result_json


if __name__ == '__main__' :
    print(getSido())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        print(getStore(sido_code='17', gugun_code=''))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 : ')
        print(getStore(gugun_code=gugun))
