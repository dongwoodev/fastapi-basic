from typing import Optional, List

from pydantic import BaseModel, HttpUrl, EmailStr
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class Item(BaseModel):
    """
    ## Item 클래스
    - name : string 타입 
    - price : float 타입 
    - amount : int 타입 (default = 0)   
    """
    name : str
    price : float
    amount : int = 0

class User(BaseModel):
    """
    ## User 클래스
    ### pydantic.BaseModel
    파이썬의 데이터클래스와 비슷한 역할
    - name : string 타입 
    - password : string 타입
    - avatar_url : pydantic에서는 자주쓰이는 타입들을 제공하고 검증도 합니다. Http_url도 그중 하나입니다. (이메일 주소, 파일 경로, 우편번호 등등)
    - inventory : 중첩 모델
    """
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = [] # Item 클래스를 리스트타입으로

# 응답
@app.post("/users/")
def create_user(user: User): 
    return user 

# 요청
@app.get("/users/me")
def get_user():
    fake_user = User(
        name="admin",
        password="1234",
        inventory=[
            Item(name="바람의 검", price=1_0000_000),
            Item(name="다이아몬드 방패", price=1_000_000),
        ]
    )
    return fake_user

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# 실무에서 비밀번호는 반드시 암호화 해야 합니다. 여기서는 예제이므로...
# http :8000/users/me
# http :8000/users/ name="warrior" password=q1w2e3r4t5y6 inventory:='[{"name":"나무 검", "price":10.0, "amount":99}]'
# := wallous operator