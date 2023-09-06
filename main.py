from fastapi import FastAPI, Header, Depends, HTTPException

app = FastAPI()


items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})


async def verify_token(x_token: str = Header(...)) -> None:
    if len(x_token) < 10: # 토큰의 길이가 10보다 작으면 에러 발생
        raise HTTPException(401, detail="Not authorized")


@app.get("/items", dependencies=[Depends(verify_token)]) # 토큰 검사, 반드시 리스트
async def get_items():
    return items

"""
DI를 함수의 매개변수가 아닌 route의 데코레이터로 활용하기

"""