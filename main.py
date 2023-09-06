from fastapi import FastAPI, HTTPException, status

app = FastAPI()

users = {
    1: {"name": "Fast"},
    2: {"name": "Slow"},
    3: {"name": "API"},
}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # 전달 받은 user_id가 users의 key값에 없으면 에러 발생
    if user_id not in users.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"<User: {user_id}> is not exists.",
        )
    # 존재하면 아래처럼 리턴
    return users[user_id]

"""
일부로 에러 발생시키기
"""