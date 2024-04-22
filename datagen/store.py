import mysql.connector
from faker import Faker
import random
from datetime import datetime
import pymysql
import csv



fake = Faker('ko-KR')
db_connection = mysql.connector.connect(
    host="192.168.122.110",
    port="30829",
    user="root",
    password="root",
    database="data"
)

def store(count):
    print("start")
    # MySQL connection settings
    cursor = db_connection.cursor()
    
    delete_all_data(cursor)

    insert_category_data(cursor)

    for i in range(0, count):
    # Insert store data
        print("insert")
        store_id = insert_store_data(cursor)
        # Insert delivery information data
        insert_delivery_data(cursor, store_id)
        # Insert category data
        # Insert store category data
        insert_store_category_data(cursor, store_id)

    # Close MySQL connection
    cursor.close()
    db_connection.close()
    print("end")

# MySQL connection settings


# 이미 선택된 UUID를 저장할 set
selected_uuids = set()

def randomUuidPicker():
    with open('store_uuids.csv', newline='') as f:
        reader = csv.reader(f)
        uuids = [row[0] for row in reader if row[0] not in selected_uuids]  # 중복되지 않는 UUID만 선택
        if not uuids:
            return None  # 모든 UUID가 이미 선택되었을 경우
        selected_uuid = random.choice(uuids)
        selected_uuids.add(selected_uuid)  # 선택된 UUID를 저장
        return selected_uuid



# Faker instance creation
# 한국데이터로 만들기


company_nick = ['','맛있는', '황금', '진한', '싱싱한', '따뜻한', '향긋한', '신선한', '기분 좋은', '착한', '빠른', '선명한', 
                '화려한', '순수한', '똑똑한', '밝은', '행복한', '신나는', '찬란한', '고운', '깨끗한', '따뜻한', '신비로운', 
                '최고', '하나', '오빠네', '진짜', '근성', '노력', '아영이네', '명인', '악마', '마약', '엽기', '신전']


company_region = ['', '서울', '인천', '부산', '강남', '포천', '뉴욕', '쌍문동', '수유동', '분당', '런던', '울산', '전주', '광주', 
                  '일산', '평양', '백두', '양평', '춘천', '의정부', '마포', '해운대', '부천', '영등포', '동대문', '마포', '성북', 
                  '금천', '용산', '중랑', '금천', '서초', '동작', '강서', '송파', '강북', '광진', '서초', '송파', '은평', '구로',
                    '강동', '강남', '양천', '도봉', '용산', '종로', '중구', '광진', '동작', '서초', '서대문', '성북', '은평', '금천', 
                    '강서', '구로', '송파', '마포', '중랑', '양천', '도봉', '강남', '영등포', '서초', '종로', '중구', '성동', '관악', 
                    '동대문', '마포', '강동', '노원', '서초', '중랑', '구로', '강서', '은평', '성북', '양천', '도봉', '용산', '금천', 
                    '중구', '종로', '서초', '동작', '성동', '강남']

company_menu = ['', '치킨', '피자', '짜장면', '회', '떡볶이', '라면', '칼국수', '냉면', '국수', '족발', '삼겹살', '순대', '곱창', 
                '보쌈', '쭈꾸미', '막창', '갈비탕', '해장국', '떡국', '김치찌개', '부대찌개', '된장찌개', '순두부찌개', '김치볶음밥', '오므라이스', 
                '불고기', '짬뽕', '짜장면', '짬뽕밥', '우동', '소바', '감자탕', '청국장', '비빔밥', '육개장', '설렁탕', '곰탕', '육회', '카레',
                  '찜닭', '닭볶음탕', '탕수육', '깐풍기', '양념치킨', '후라이드치킨', '간장치킨', '양념갈비', '김밥', '샌드위치', '파스타', '햄버거',
                    '쌀국수', '닭갈비', '갈비찜', '생선구이', '해물찜', '양념게장', '오징어숙회', '계란찜', '제육볶음', '삼겹살구이', '쫄면', '비빔냉면', 
                    '물냉면', '비빔밥', '간장불고기', '양념불고기', '매운갈비찜', '해물누룽지탕', '김치전', '해물파전', '닭발', '소주', '맥주', '막걸리', 
                    '청하', '핫바', '간장게장', '양념게장', '마파두부', '깐풍기', '마라탕', '마라샹궈', '마라샹궈', '쫄면', '떡갈비', '훈제오리', '콩나물국밥', '소불고기', '김치찜', '계란국',
                    '우동', '삼계탕', '쌈밥', '콩나물국밥', '순두부찌개', '곱창', '보쌈', '두부조림', '막창', '쭈꾸미', '해장국', '곱창',
                  '족발', '죽', '우럭구이', '보리밥', '설렁탕', '아귀찜', '낙지볶음', '꽃게탕', '바지락순두부', '삼겹살', '양념치킨', 
                  '오삼불고기', '족발', '매운닭발', '철판볶음밥', '매운갈비찜', '양념갈비', '부대찌개', '설렁탕', '콩비지찌개', '소고기국밥',
                    '육회', '매운족발', '옻닭', '매운갈비찜', '통마늘닭발', '불고기', '장조림', '오징어덮밥', '매운족발', '수제비', '닭발', 
                    '삼겹살', '오삼불고기', '초밥', '해물찜', '삼계탕', '갈치조림', '연어회', '초밥', '해물탕', '육개장', '알밥', '쌈밥', 
                    '부대찌개', '닭볶음탕', '육회비빔밥', '갈치구이', '장어구이', '쌈밥', '고등어조림', '곰탕', '알탕',
                    '루','각','반점',
                    '커피', '케이크', '티라미수', '라떼', '차', '버블티'
                ]

categories = {
    '족발,보쌈': ['족발', '보쌈'],
    '돈까스,회,일식': ['돈까스', '회', '초밥', '라면', '카레', '수산', '연어', '초밥'],
    '고기,구이': ['삼겹살', '곱창', '막창', '닭갈비', '불고기', '숯불구이', '스테이크', '생선구이', '오리고기', '오삼불고기'],
    '피자': ['피자'],
    '찜,탕,찌개': ['김치찌개', '순두부찌개', '된장찌개', '부대찌개', '해물탕', '곰탕', '국밥', '삼계탕', '양념게장', '갈비탕', '소고기 국밥', '쭈꾸미', '해장국', '오리탕', '보신탕', '옻닭', '설렁탕', '곰탕', '아구찜', '해물찜'],
    '양식': ['스파게티', '스테이크', '샐러드', '파스타'],
    '중식': ['루', '각', '반점', '짬뽕', '마라'],
    '아시안': ['팟타이', '쌀국수', '커리', '뿌빳뽕커리'],
    '치킨': ['후라이드 치킨', '양념치킨', '간장치킨', '치킨텐더', '치킨너겟', '치킨버거'],
    '백반,죽,국수': ['김치볶음밥', '오므라이스', '김밥', '떡볶이', '냉면', '쌀국수', '라면', '죽', '덮밥', '칼국수', '청국장', '알밥', '쌈밥', '육회비빔밥', '파전'],
    '버거': ['햄버거', '치즈버거', '더블버거', '베이컨버거'],
    '분식': ['떡볶이', '김밥', '라면', '튀김', '순대', '떡튀순'],
    '카페,디저트': ['커피', '라떼', '아메리카노', '스무디', '케이크', '빙수', '파르페', '와플', '크로플', '버블티']
}


ingredient_from = ['김치: 국산 ', '김치: 중국산 ', '돼지고기: 캐나다산 ', '돼지고기: 국산 ', '소고기: 국산 ', '소고기: 미국산 ', '소고기: 호주산 ', '고등어: 노르웨이 ', "닭: 국산 ", '닭: 브라질산 ', '어류: 국산 ', '오리:국산 ', '어폐류: 국산 ', '참치: 원양산 ', '밀가루: 미국산 ', '밀가루 캐나다산 ',
                   '쌀: 국산 ']

def generate_ingredient_from():
    count = random.randint(1, 10)
    ret = "원산지 표기 : "
    selected_ingredients = set()  # 이미 선택된 원산지를 기록할 집합 생성
    for _ in range(count):
        ingredient = random.choice(ingredient_from)
        while ingredient in selected_ingredients:  # 이미 선택된 원산지와 겹치는지 확인
            ingredient = random.choice(ingredient_from)
        selected_ingredients.add(ingredient)  # 선택된 원산지를 기록
        ret += ingredient
    return ret




def generate_company_name(categoryId):
    nick = random.choice(company_nick)
    region = random.choice(company_region)
    menu = random.choice(categories[categoryId])
    return f"{nick}{region} {menu}"

def generate_business_hours():
    # 전체 24시간 중에서 랜덤한 운영 시작 시간 선택
    start_hour = fake.random_int(0, 15)  # 최대 16시까지 선택 (8시간 이상 운영)
    start_minute = fake.random_element([0, 30])  # 00분 또는 30분 선택
    # 운영 시간은 최소 8시간 이상으로 설정
    end_hour = fake.random_int(start_hour + 8, 23)  # 최소 8시간 이상 운영
    end_minute = fake.random_element([0, 30])  # 00분 또는 30분 선택

    # 만약 24시간 영업일 경우에는 23:59도 고려
    if end_hour == 23 and end_minute == 30:
        end_minute = 59

    # 선택된 시간을 시:분 형식으로 변환
    start_time = f"{start_hour:02d}:{start_minute:02d}"  # 시간과 분을 두 자리 숫자로 포맷
    end_time = f"{end_hour:02d}:{end_minute:02d}"  # 시간과 분을 두 자리 숫자로 포맷

    # 운영시간 문자열 생성
    business_hours = f"{start_time} - {end_time}"
    print(business_hours)
    return business_hours



# Function to generate store data
def generate_store_data():
    # 카테고리 중 하나를 무작위로 선택
    random_category = random.choice(list(categories.keys()))
    store_id = randomUuidPicker()
    if store_id is None:
        return None  # 더 이상 사용 가능한 UUID가 없음
    # 이후 로직은 store_id를 사용하여 다른 데이터를 생성하는 부분입니다.
    # 예시: fake.uuid4() 대신 store_id를 사용하고 있습니다.
    return (
        store_id,  # Store ID
        random.choice(['open', 'close']),  # Status
        generate_company_name(random_category),  # Name 별명 + 지역 + 음식 으로 랜덤화 시키기
        fake.address() + fake.address_detail(),  # Address
        generate_business_hours(),  # Business hours
        fake.day_of_week(),  # Day off
        fake.sentence(),  # Description
        fake.random_int(8000, 12000, 1000),  # Min orders
        fake.phone_number(),  # Phone number
        fake.name(),  # Owner
        fake.address(),  # Taxpayer address
        fake.random_number(10),  # Taxpayer ID number
        generate_ingredient_from(),  # Ingredients
        datetime.now(),  # Created on
        datetime.now()  # Last updated on
    )

# Function to generate delivery information data
def generate_delivery_data(store_id):
    return (
        fake.uuid4(),  # Delivery info ID
        store_id,  # Store ID
        random.choice(['motorcycle', 'car', 'bicycle']),  # Delivery type
        fake.random_int(1000, 5000, 500),  # Min fee
        fake.random_int(5000, 10000, 500),  # Max fee
        fake.random_int(1, 10),  # Max distance
        datetime.now(),  # Created on
        datetime.now()  # Last updated on
    )

# Function to generate category data
def generate_category_data(category):
    category_id = list(categories.keys()).index(category) + 1  # 카테고리의 인덱스를 이용하여 ID 설정
    category_name = category
    sub_categories = ', '.join(categories[category])  # 서브카테고리 리스트를 문자열로 변환
    return (
        category_id,  # Category ID
        None,  # Parent category ID 
        category_name,  # Name
        sub_categories,  # Description: 서브카테고리 리스트
        datetime.now(),  # Created on
        datetime.now()  # Last updated on
    )

# Function to generate store category data
def generate_store_category_data(store_id):
    category_id = random.randint(1, 13)
    return (
        fake.uuid4(),  # Store category ID
        store_id,  # Store ID
        category_id,  # Category ID
        datetime.now(),  # Created on
        datetime.now()  # Last updated on
    )

# Function to insert store data
def insert_store_data(cursor):
    query = "INSERT INTO store (store_id, status, name, address, business_hours, day_off, description, min_orders, phone_number, owner, taxpayer_address, taxpayer_id_number, ingredients, created_on, last_updated_on) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    store_data = generate_store_data()
    cursor.execute(query, store_data)
    db_connection.commit()
    return store_data[0]  # Return the newly inserted store ID

# Function to insert delivery information data
def insert_delivery_data(cursor, store_id):
    query = "INSERT INTO delivery_info (delivery_info_id, store_id, delivery_type, min_fee, max_fee, max_dist, created_on, last_updated_on) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    delivery_data = generate_delivery_data(store_id)
    cursor.execute(query, delivery_data)
    db_connection.commit()

# Function to insert category data
def insert_category_data(cursor):
    query = "INSERT INTO category (category_id, parent_category_id, name, description, created_on, last_updated_on) VALUES (%s, %s, %s, %s, %s, %s)"
    for category in categories:
        category_data = generate_category_data(category)
        cursor.execute(query, category_data)
    db_connection.commit()
    return category_data[0]  # Return the newly inserted category ID

# Function to insert store category data
def insert_store_category_data(cursor, store_id):
    query = "INSERT INTO store_category (store_category_id, store_id, category_id, created_on, last_updated_on) VALUES (%s, %s, %s, %s, %s)"
    store_category_data = generate_store_category_data(store_id)
    cursor.execute(query, store_category_data)
    db_connection.commit()


def delete_all_data(cursor):
    # store_category 테이블 데이터 삭제
    cursor.execute("DELETE FROM store_category")
    # delivery_info 테이블 데이터 삭제
    cursor.execute("DELETE FROM delivery_info")
    # store 테이블 데이터 삭제
    cursor.execute("DELETE FROM store")
    # category 테이블 데이터 삭제
    cursor.execute("DELETE FROM category")

store(10000)

