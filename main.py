from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/") # trailling slash : 307 오류 발생 주의
def get_user(limit: Optional[int] = None): # 옵셔널 타입 힌트 : Int 거나 Null일 수도 있다. 입력을 하지 않으면 None 발생 
    return {"limit": limit}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# http ':8000/users?limit=1'
# http ':8000/users/?limit=1'
# # http ':8000/users/?'