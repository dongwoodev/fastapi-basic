"""
### 1. DB
1. Engine 만들기
- mysql+pymysql://user:pw@local:port/db 순으로 DB 주소를 작성하여 engine을 만듭니다.
2. SessionMaker
- 만든 엔진을 토대로 Session을 생성합니다.


"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://admin:1234@0.0.0.0:3306/dev") # DB 주소 입력 (DB 연결할 엔진)

# 세션 생성
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base() # 모델 정의를 위한 부모 클래스 생성

