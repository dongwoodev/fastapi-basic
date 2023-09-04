from typing import Optional

from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class User(BaseModel):
    """
    ## User 클래스(요청)
    - name : String
    - password : String
    - avatar_url : HttpUrl
    """
    name: str = "fastapi"
    password: str
    avatar_url: HttpUrl = None


@app.post(
    "/include",
    response_model=User,
    response_model_include={"name", "avatar_url"},  # Set 타입. List도 괜찮습니다.
)
def get_user_with_include(user: User):
    return user


@app.post(
    "/exclude",
    response_model=User,
    response_model_exclude={"password"},
)
def get_user_with_exclude(user: User):
    return user


@app.post(
    "/unset",
    response_model=User,
    response_model_exclude_unset=True, # 정해져있지 않거나 null인 경우 exclude
)
def get_user_with_exclude_unset(user: User):
    # 요청은 User 응답은 app.post() 같이
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""
자동 생성 문서에 표현되지 않아 추천하지 않는 방법이지만, 
데코레이터 메소드의 다음 매개변수 중 하나를 사용하여 응답 형태를 바꿀 수 있습니다. 

즉, 실제 API와 Docs에 schema와 틀리게 됩니다. 그래서 추천하지 않습니다.

- response_model_include
- response_model_exclude
- response_model_exclude_unset
"""