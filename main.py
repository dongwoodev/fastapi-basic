from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# 에러 클래스 정의
class SomeError(Exception):
    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

    def __str__(self):
        return f"<{self.name}> is occured. code: <{self.code}>"


app = FastAPI()

#  에러 핸들러 추가
@app.exception_handler(SomeError)
async def some_error_handler(request: Request, e: SomeError):
    return JSONResponse(
        content={"message": f"error is {e.name}"}, status_code=e.code
    )


@app.get("/error")
async def get_error():
    raise SomeError("Hello", 400)
"""
사용자 정의 에러

에러 핸들러가 있으면 정확히 어떤 에러인지 보여줄 수 있습니다.
"""