from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {'username' : username}

"""
python-multipart==0.0.6
aiofiles==23.2.1

mount : static(정적 파일)을 임포트할 수 있게 끔 도와줍니다. (가장 앞단에 있는 매개변수는 엔드포인트입니다.)
Form : fastapi에서 Form을 임포트해서 username을 반환합니다.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload  

## 주의
Form 형식을 사용한 경우에는 Json 형식을 사용할 수 없습니다.
이유는 미디어 타입이 application/json이 아니라 application.x-www-form-urlencoded 이기 때문입니다. 
이거는 HTTP 스펙에 관한 문제입니다.
"""