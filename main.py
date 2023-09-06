from typing import Any, Optional, Dict

from fastapi import FastAPI, HTTPException
# from starlette.exceptions import HTTPException 
# FastApi가 Starlette를 상속받지만 starlette은 헤더를 사용할 수 없습니다.


class SomeFastAPIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            status_code=status_code, detail=detail, headers=headers
        )


app = FastAPI()


@app.get("/error")
async def get_error():
    raise SomeFastAPIError(500, "Hello")

"""
사용자 정의 에러

에러 핸들러가 없이 실행 가능합니다.
 이는 starlette의 미들웨어가 HTTPException을 처리하고 있기 때문입니다. (기본 HTTP 에러)
"""