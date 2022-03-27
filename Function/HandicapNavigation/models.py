import json

from django.db import models


class Convinienttable(models.Model):
    id = models.IntegerField(primary_key = True,blank=True)
    고유번호 = models.IntegerField(blank=True, null=True)
    시설명 = models.TextField(blank=True, null=True)
    담당구 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)
    연락처 = models.TextField(blank=True, null=True)
    홈페이지 = models.TextField(blank=True, null=True)
    추천수 = models.IntegerField(blank=True, null=True)
    주출입구_접근로_여부 = models.TextField(blank=True, null=True)
    주출입구_높이차이_제거_여부 = models.TextField(blank=True, null=True)
    장애인용_승강기_여부 = models.TextField(blank=True, null=True)
    장애인_화장실_여부 = models.TextField(blank=True, null=True)
    장애인용_관람석_이용가능_여부 = models.TextField(blank=True, null=True)
    장애인_매표소_여부 = models.TextField(blank=True, null=True)
    시각장애인_편의서비스_여부 = models.TextField(blank=True, null=True)
    청각장애인_편의서비스_여부 = models.TextField(blank=True, null=True)
    안내_서비스_여부 = models.TextField(blank=True, null=True)
    휠체어_대여_여부 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)
    시설분류 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'convinienttable'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Libraries(models.Model):
    도서관_일련번호 = models.IntegerField(blank=True, primary_key=True)
    도서관명 = models.TextField(blank=True, null=True)
    구_코드 = models.IntegerField(blank=True, null=True)
    구명 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)
    전화번호 = models.TextField(blank=True, null=True)
    홈페이지_url = models.TextField(blank=True, null=True)
    운영시간 = models.TextField(blank=True, null=True)
    정기_휴관일 = models.TextField(blank=True, null=True)
    도서관_구분명 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libraries'



class Pabulicparkingspot(models.Model):
    주차장코드 = models.IntegerField(blank=True, null=True)
    주차장명 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)
    주차장_종류 = models.TextField(db_column='주차장 종류', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    주차장_종류명 = models.TextField(db_column='주차장 종류명', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    운영구분 = models.IntegerField(blank=True, null=True)
    운영구분명 = models.TextField(blank=True, null=True)
    전화번호 = models.TextField(blank=True, null=True)
    총_주자면 = models.IntegerField(db_column='총 주자면', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    유무료구분 = models.TextField(blank=True, null=True)
    유무료구분명 = models.TextField(blank=True, null=True)
    야간무료개방여부 = models.TextField(blank=True, null=True)
    야간무료개방여부명 = models.TextField(blank=True, null=True)
    평일_운영_시작시각_hhmm_field = models.TextField(db_column='평일 운영 시작시각(HHMM)', blank=True, null=True)
    평일_운영_종료시각_hhmm_field = models.IntegerField(db_column='평일 운영 종료시각(HHMM)', blank=True, null=True)
    주말_운영_시작시각_hhmm_field = models.TextField(db_column='주말 운영 시작시각(HHMM)', blank=True, null=True)
    주말_운영_종료시각_hhmm_field = models.IntegerField(db_column='주말 운영 종료시각(HHMM)', blank=True, null=True)
    공휴일_운영_시작시각_hhmm_field = models.TextField(db_column='공휴일 운영 시작시각(HHMM)', blank=True, null=True)
    공휴일_운영_종료시각_hhmm_field = models.IntegerField(db_column='공휴일 운영 종료시각(HHMM)', blank=True, null=True)
    최종데이터_동기화_시간 = models.TextField(db_column='최종데이터 동기화 시간', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    토요일_유_무료_구분 = models.TextField(db_column='토요일 유,무료 구분', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    토요일_유_무료_구분명 = models.TextField(db_column='토요일 유,무료 구분명', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    공휴일_유_무료_구분 = models.TextField(db_column='공휴일 유,무료 구분', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    공휴일_유_무료_구분명 = models.TextField(db_column='공휴일 유,무료 구분명', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    월_정기권_금액 = models.IntegerField(db_column='월 정기권 금액', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    노상_주차장_관리그룹번호 = models.TextField(db_column='노상 주차장 관리그룹번호', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    기본_주차_요금 = models.IntegerField(db_column='기본 주차 요금', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    기본_주차_시간_분_단위_field = models.IntegerField(db_column='기본 주차 시간(분 단위)', blank=True, null=True)
    추가_단위_요금 = models.IntegerField(db_column='추가 단위 요금', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    추가_단위_시간_분_단위_field = models.IntegerField(db_column='추가 단위 시간(분 단위)', blank=True, null=True)
    버스_기본_주차_요금 = models.IntegerField(db_column='버스 기본 주차 요금', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    버스_기본_주차_시간_분_단위_field = models.IntegerField(db_column='버스 기본 주차 시간(분 단위)', blank=True, null=True)
    버스_추가_단위_시간_분_단위_field = models.IntegerField(db_column='버스 추가 단위 시간(분 단위)', blank=True, null=True)
    버스_추가_단위_요금 = models.IntegerField(db_column='버스 추가 단위 요금', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    일_최대_요금 = models.TextField(db_column='일 최대 요금', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    주차장_위치_좌표_위도 = models.FloatField(db_column='주차장 위치 좌표 위도', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    주차장_위치_좌표_경도 = models.FloatField(db_column='주차장 위치 좌표 경도', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'pabulicparkingspot'


class Seoulparking(models.Model):
    시설명 = models.TextField(blank=True,  primary_key=True)
    담당구 = models.TextField(blank=True, null=True)
    주차가능면 = models.IntegerField(blank=True, null=True)
    담당구_0_field = models.TextField(db_column='담당구_[0]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    주소 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)
    시설분류 = models.TextField(blank=True, null=True)
    세부분류 = models.TextField(blank=True, null=True)
    장애인_주차칸_여부 = models.TextField(db_column='장애인 주차칸 여부', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'seoulparking'


class Trainconvinienttable(models.Model):
    구 = models.TextField(blank=True, null=True)
    역명 = models.TextField(blank=True,  primary_key=True)
    승강기_개수 = models.IntegerField(db_column='승강기 개수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    에스컬레이터_개수 = models.IntegerField(db_column='에스컬레이터 개수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    휠체어리프트_개수 = models.IntegerField(db_column='휠체어리프트 개수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    전동휠체어_급속충전기_개수 = models.IntegerField(db_column='전동휠체어 급속충전기 개수', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    경도 = models.FloatField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainconvinienttable'


class Wheelcharger(models.Model):
    시설명 = models.TextField(blank=True,  primary_key=True)
    시도명 = models.TextField(blank=True, null=True)
    시군구명 = models.TextField(blank=True, null=True)
    시군구코드 = models.IntegerField(blank=True, null=True)
    소재지도로명주소 = models.TextField(blank=True, null=True)
    소재지지번주소 = models.TextField(blank=True, null=True)
    위도 = models.FloatField(blank=True, null=True)
    경도 = models.FloatField(blank=True, null=True)
    설치장소설명 = models.TextField(blank=True, null=True)
    평일운영시작시각 = models.TextField(blank=True, null=True)
    평일운영종료시각 = models.TextField(blank=True, null=True)
    토요일운영시작시각 = models.TextField(blank=True, null=True)
    토요일운영종료시각 = models.TextField(blank=True, null=True)
    공휴일운영시작시각 = models.TextField(blank=True, null=True)
    공휴일운영종료시각 = models.TextField(blank=True, null=True)
    동시사용가능대수 = models.IntegerField(blank=True, null=True)
    공기주입가능여부 = models.TextField(blank=True, null=True)
    휴대전화충전가능여부 = models.TextField(blank=True, null=True)
    관리기관명 = models.TextField(blank=True, null=True)
    관리기관전화번호 = models.TextField(blank=True, null=True)
    데이터기준일자 = models.TextField(blank=True, null=True)
    제공기관코드 = models.IntegerField(blank=True, null=True)
    작업일시 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wheelcharger'
