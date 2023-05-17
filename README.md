# Data Visualization Project

장애인을 위한 교통 편의시설 지도형 웹 서비스 입니다. <br><br>
장애인들이 이용할 수 있는 편의시설을 카테고리별로 지도에 표시하고, <br>
서울시 장애인 편의시설 시각화 및 현황 분석을 통해 추가입지 선정을 제안합니다.

### 🥇 삼성 멀티캠퍼스 공공데이터 시각화 프로젝트 경진대회 최우수상 수상

`김경미`, `박현수`, `박혜인`: 데이터 수집 및 전처리, EDA <br>
`성낙원`. `이재필(팀장)`, `최재영`: FE, BE

## 1. 프로젝트 목표

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/76639736-5d63-4445-bf89-33b58f8bba64)

- '장애인' 키워드에 대한 트렌드 분석으로, 최근 5년 간 '장애인' 뉴스 키워드를 분석
- '복지' 분야의 Top 60에 해당하는 뉴스 키워드를 분석한 결과, *'서울', '편의시설'과 관련된 키워드*가 많이 생성됨
- 이외에도 장애인을 위한 서비스와 앱/사이트가 미흡한 선행조사를 통해, 장애인들이 편리하게 이용할 수 있는 장애인 편의시설 웹 서비스를 구현함

## 2. 데이터 분석 및 시각화

### (1) 활용 데이터 목록

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/2cb65c2b-d5f9-4e59-98a5-5ed823e3ceab)

- 대부분의 데이터는 [공공데이터포털](https://www.data.go.kr/)에서 다운 받아 사용
- 서울특별시 주차장 목록은 [서울특별시 주차정보안내시스템](https://parking.seoul.go.kr/)에서 크롤링 후 전처리 하여 사용
- 소셜 빅데이터 기반 보건복지 이슈 및 동향 분석은 [빅카인즈](https://www.bigkinds.or.kr/)에서 5개년 키워드 데이터를 다운 받아 사용

### (2) 구 별 장애인 등록자 수와 총 편의시설 분포량의 상관관계 검정 (가설검정)

> 가설 : 구 별로 등록된 장애인 수가 많을수록 해당 구별 편의시설도 많을 것이다

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/65357024-5ab5-4d7e-bf57-e095de280dad)

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/946afb01-e3ac-4ab2-86a4-0146f2705f12)

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/8c0584d8-4a3b-4c8d-9771-3c0966bafdd5)

```
결과적으로, 장애인 등록자 수와 총 편의시설 수 사이에는 상관관계가 없다
즉, 장애인 등록자 수가 많아도 편의시설 수가 부족할 수 있다
```

### (3) 장애인 교통 편의시설 현황 : 콜택시, 주차장, 지하철, 저상버스

#### ① 콜택시

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/668a8be3-adef-4003-b205-3dd3e2559df9)

* 시간대별 장애인 콜택시 이용 현황을 살펴본 결과, 아침 출근시간대에 콜택시 이용률이 증가하고, **점심 시간대인 11~14시** 사이에 이용률이 가장 높음을 확인할 수 있음
* 요일별 장애인 콜택시 이용 현황을 살펴본 결과, 평일 이용률이 가장 높고, 시간으로는 **점심 > 아침 > 저녁 > 심야 시간대** 순서로 이용률이 높음

#### ② 주차장

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/b1b1195c-99dd-4ade-bfb7-206abffbaf82)

* 민영주차장에 대해서는 장애인 주차칸에 대해 명시된 법령이 나와있지 않아, 이를 제외하고 공영주차장에 대해서만 분석을 진행함
* 각 구에서 보유한 공영주차장 수는 면적으로 나타내고, 해당 구내의 장애인 주차 가능 여부는 색깔로 표기함

```
결과적으로, 강남구가 주차장 수가 가장 많았고, 장애인 주차 가능 비율도 가장 높았음
하지만, 동작구의 경우, 장애인 주차가능 비율이 40% 밖에 되지 않으므로 장애인들이 주차장을 이용하는 데에 상당한 불편함을 겪을 수 음음
```

#### ③ 지하철

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/7ca30442-0c80-4c96-884e-38b8436d592f)

* folium을 활용하여, 구 별 지하철 내의 장애인 전체 편의시설 분포를 맵핑
* **장애인 수가 많은 강서구, 노원구에 필요한 편의시설이 부족**
* 송파구, 강남구 순으로 다른 구에 비해 상대적으로 많은 편의시설 보유

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/469ff73f-bf4f-41fe-ade0-bc85c3c0549f)

* folium을 활용하여, 구 별 지하철 내 휠체어 리프트 분포를 맵핑한 결과, 각 구 별 대부분 0~5개의 휠체어 리프트가 설치되어 있음
* 휠체어 급속충전기의 경우, 각 구 별 대부분 0~10개 미만의 휠체어 급속 충전기가 설치되었으며, **10개 이상 설치된 구는 존재하지 않음**

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/d31cdb05-51a7-4082-9592-9d0cacaa3635)

* 각 구 별 15~30개의 승강기가 설치되어 있음

```
지하철 내 장애인 편의시설 분포는 장애인 수 분포에 비례하지 않음
장애인 교통 약자를 위한 편의시설의 절대적인 수가 작음
```

#### ④ 저상버스

* 장애인 1만명 당 필요한 저상 버스 수를 비교분석

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/9818b097-1bf1-41f4-b714-c1744b4884c0)

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/6fb2b06e-c638-4297-9783-7880ec6e7aba)

```
막대 그래프 상 평균 2대의 버스가 올 때, 저상 버스는 1대가 옴.
즉, 장애인들은 버스 1번을 타기 위해, 버스 2대가 지나갈 시간을 기다려야 함

장애인들의 이동권 보장을 위해 저상 버스 보급 확대 필요
```

## 3. 장애인 교통 편의시설 개선사항 및 기대효과

* 장애인 교통 편의시설 개선할 점

  1. 서울시 내 전체 장애인 중 지체장애인이 44%로 가장 많음
  ![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/1d68ecaa-6f01-4f7c-9b29-530307015159)


  2. 장애인 편의시설 수가 턱없이 부족한 현실
      - 편의시설 1개당 소화해야 하는 자앵인의 평균 인구 수는 241명
      - 강북구는 편의시설 1개당 약 800명의 장애인이 사용해야 함


  3. 편의시설의 절대적인 수 증진 필요
  ![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/f54c7d6b-655c-460d-b415-30ca1c781928)
  
      - 장애인 인원 수 별 설치가 필요한 편의시설 기준이 존재하지 않음
      - 국가적인 기준을 만들고, 이를 관리할 필요성 증대


* 개선사항에 대한 기대효과

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/1b0e4e52-c636-48de-80f8-dc632c506180)


## 4. 핸디나비(HandiNavi) 서비스 소개 및 구현

* 서비스 구현에 사용한 기술 : `html`, `css`, `js`, `Django`, `MySQL`
* 이외에 기타 Naver MAP API를 받아 구현에 활용

![image](https://github.com/Hyeeein/HandiNavi/assets/81239567/c08535e1-8dca-4d81-aadc-0dfdb478b26c)


## 5. 최종 포트폴리오

* [발표 자료](https://github.com/Hyeeein/HandiNavi/blob/master/Documents/%5B%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C%5DHandiNavi.pdf)
* [포트폴리오](https://github.com/Hyeeein/HandiNavi/blob/master/Documents/%5B%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4%5DHandiNavi.pdf)
