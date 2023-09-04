from typing import Optional, List

from pydantic import BaseModel, Field # Field
from fastapi import FastAPI, Query, Path
import uvicorn

app = FastAPI()

class Item(BaseModel):
    """
    ## Item 클래스
    - name
    - price : 0초과
    - amount : 1, 0초과 100이하
    """
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    # Field(name(필수), 1~100)
    price: float = Field(None, ge=0) # default = None
    amount: int = Field(
        default=1, 
        gt=0,
        le=100, #less than equal
        title="수량",
        description="아이템 갯수. 1~100 개 까지 소지 가능",
    )


@app.post("/users/{user_id}/item") # 원래는 user_id에 대한 검증도 필요합니다.
def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""
# Field 데이터 정의
"""