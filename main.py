from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/{user_id}")
# @app.get("/users/{user_id:int}") # Flask 방식 : 함수에 대한 매개변수를 찾아볼 수 없다. ex) user_id.{}
def get_user(user_id: int): # 타입 힌트
    return {"user_id": user_id}

if __name__ == "__main__":
    # uvicorn.run(app)
    uvicorn.run("main:app", reload=True)