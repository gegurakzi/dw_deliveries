# 배달의 민족 ERD 차원 모델링

### 1. ERD 설계

> https://www.erdcloud.com/d/MMaW68NoW8Yg7vSva

### 2. 데이터 생성

- `domain.models`  
  SQLAlchemy ORM을 위해 정의한 테이블 레코드 객체들
- `application.services`  
  `사용자 가입`, `가족 계정 생성` 등 서비스 기능을 중심으로 더미 데이터를 저장하도록 구성한 로직
- `application.modelers`  
  랜덤한 더미 객체를 반환하는 함수들
- `application.randomizer`  
  다양한 랜덤 값을 반환하는 유틸성 함수들
- `main.py`  
  실행 스크립트