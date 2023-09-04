from enum import Enum
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 열거형 지원(다중상속도 지원)
class UserLevel(str, Enum):
    a = "a"
    b = "b"
    c = "c"

@app.get("/users/") # trailling slash : 307 오류 발생 주의
def get_user(grade: UserLevel): 
    return {"grade" : grade} 

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# http ":8000/users/?grade=a"
# http ":8000/users/?grade=d"

# 기본값을 작성하는 경우
# # def get_user(grade: UserLevel = "a"): #하드코딩 
# def get_user(grade: UserLevel = UserLevel.a): # 직접 작성
# http ":8000/users/"
# 열거형의 기본값을 적을 경우 하드코딩 하는 것보다 직접 작성하는 게 좋습니다.
