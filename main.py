from typing import Optional, List

from fastapi import FastAPI, Cookie, Header
import uvicorn

app = FastAPI()

@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    # 헤더를 받아 헤더 반환
    return {"X-Token": x_token}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""
# 쿠키
http :8000/cookie Cookie:ga=123.123.123

from fastapi import FastAPI, Cookie
import uvicorn

app = FastAPI()

@app.get("/cookie")
def get_cookie(ga: str = Cookie(None)):
    return {"ga":ga}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# 헤더
X- 접두어는 사용자 정의 헤더라는 것을 의미합니다. 
반드시 이렇게 할 필요는 없지만, 표준 헤더와 구분짓기 위해 사용합니다. 
http :8000/header X-Token:some.secret.token
"""