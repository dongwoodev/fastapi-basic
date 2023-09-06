from typing import Any, Optional, Dict

from fastapi import FastAPI, Depends

app = FastAPI()


items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})


async def get_q(q: Optional[str] = None) -> Optional[str]:
    return q


async def func_params_with_sub(
    q: Optional[str] = Depends(get_q), offset: int = 0, limit: int = 100
) -> Dict[str, Any]:
    return {"q": q, "offset": offset, "limit": limit}


@app.get("/items/func/sub")
async def get_items_with_func_sub(
    params: dict = Depends(func_params_with_sub)
):
    response = {}
    if params["q"]:
        response.update({"q": params["q"]})

    result = items[params["offset"]: params["offset"] + params["limit"]]
    response.update({"items": result})

    return response

"""
DI의 DI : 종속성의 종속성
"""