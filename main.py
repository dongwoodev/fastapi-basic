from typing import Optional

from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI, status
import uvicorn

app = FastAPI()

class User(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"


class CreateUser(User):
    password: str


#@app.post("/users", response_model=User, status_code=201)  # 추가: status_code
@app.post("/users", response_model=User, status_code=status.HTTP_200_OK)
def create_user(user: CreateUser):
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""
status code가 201상태로 응답을 오게합니다.
원래는 200으로 옵니다.(정상적인 경우에)



"""