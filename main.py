from typing import Optional

from pydantic import BaseModel, HttpUrl, EmailStr
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class User(BaseModel):
    """
    ### pydantic.BaseModel
    파이썬의 데이터클래스와 비슷한 역할
    - name : string 타입 
    - password : string 타입
    - avatar_url : pydantic에서는 자주쓰이는 타입들을 제공하고 검증도 합니다. Http_url도 그중 하나입니다. (이메일 주소, 파일 경로, 우편번호 등등)
    """
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None

@app.post("/users")
def create_user(user: User): 
    return user 

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# 실무에서 비밀번호는 반드시 암호화 해야 합니다. 여기서는 예제이므로...
# http :8000/users name=admin password=1234
