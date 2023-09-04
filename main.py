from typing import Optional

from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 요청
class CreateUser(BaseModel):
    name: str
    password: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"


# 응답
class GetUser(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"


@app.post("/users", response_model=GetUser)  # 응답 모델
def create_user(user: CreateUser):  # 요청 모델
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# http :8000/users name=admin password=1234
## name과 password을 요청했지만 name만 응답되는 것을 확인할 수 있습니다.

"""
상속을 받아 코드 반복 최소화를 할 수 있습니다. 


from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


class User(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"

# 요청
class CreateUser(User):
    password: str


@app.post("/users", response_model=User) # 응답 모델
def create_user(user: CreateUser):
    # 반복 코드를 최소화함!
    return user
"""