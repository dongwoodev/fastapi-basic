"""
2. Model : DB 테이블 정의
- Base : Databases에서 설정했던 모듈을 상속받습니다.
- `User` : 유저 테이블 생성
"""

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)


