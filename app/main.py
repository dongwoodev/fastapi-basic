from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas # 모델과 스키마를 임포트 합니다.
from .database import SessionLocal, engine # 데이터베이스 엔진을 임포트합니다.

models.Base.metadata.create_all(bind=engine) # 데이터베이스 설정


app = FastAPI()

# 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# user를 생성하는 API
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email=user.email
    ).first()

    # 이메일이 존재하는지  이미 중복되있다면 400날리기
    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 그렇지 않으면 이메일과 패스워드를 받아 db에 저장
    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user


# user를 읽는 API
@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# pip install cryptography, SQLAlchemy, PyMySQL
# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload