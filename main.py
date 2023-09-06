from tempfile import NamedTemporaryFile
from typing import IO

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


async def save_file(file: IO):
    # s3 업로드라고 생각해 봅시다. delete=True(기본값)이면
    # 현재 함수가 닫히고 파일도 지워집니다.
    with NamedTemporaryFile("wb", delete=False) as tempfile:
        tempfile.write(file.read()) # 파일을 읽고 tempfile에 씁니다.
        return tempfile.name


@app.post("/file/store")
async def store_file(file: UploadFile = File(...)):
    path = await save_file(file.file) # tempfile을 path 저장
    return {"filepath": path}

"""
python-multipart==0.0.6

contextmanager를 사용하면 다양하게 파일 처리할 수 있습니다.

"""