from typing import Any, Optional, Dict

from fastapi import FastAPI, Depends # 의존성 주입
from pydantic import BaseModel, Field # Pydantic


app = FastAPI()

items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})

# 함수로 정의
async def func_params(
    q: Optional[str] = None, offset: int = 0, limit: int = 100
) -> Dict[str, Any]:
    return {"q": q, "offset": offset, "limit": limit}

# 클래스로 정의
class ClassParams:
    def __init__(
        self, q: Optional[str] = None, offset: int = 0, limit: int = 100
    ):
        self.q = q
        self.offset = offset
        self.limit = limit

# pydantic으로 정의
class PydanticParams(BaseModel):
    q: Optional[str] = Field(None, min_length=2) # p의 최소길이가 2
    offset: int = Field(0, ge=0) # greater than or equal , gte
    limit: int = Field(100, gt=0)

# 함수
@app.get("/items/func")
async def get_items_with_func(params: dict = Depends(func_params)):
    response = {} # 딕셔너리
    if params["q"]: # `q`가 존재하면
        response.update({"q": params["q"]}) # 추가합니다.

    result = items[params["offset"]: params["offset"] + params["limit"]] # Slicing -> offset <= x < offset+limit
    response.update({"items": result})

    return response

# 클래스
@app.get("/items/class")
async def get_items_with_class(params: ClassParams = Depends(ClassParams)):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response

# pydantic
@app.get("/items/pydantic")
async def get_items_with_pydantic(params: PydanticParams = Depends()):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response


"""
페이징 구현을 위함
http ':8000/items/pydantic?q=F'
"""