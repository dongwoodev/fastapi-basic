from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/file/size")
def get_filesize(file: bytes = File(...)):
    return {"file_size": len(file)} # 바이트열의 크기를 리턴


@app.post("/file/info")
def get_file_info(file: UploadFile = File(...)):
    return {
        "content_type": file.content_type,
        "filename": file.filename
    }

@app.post("/file/info")
async def get_file_info2(file: UploadFile = File(...)):
    file_like_obj = file.file # 존재하는 이유는 비동기때문?
    contents = await file.read()

    return {
        "content_type": file.content_type,
        "filename": file.filename,
    }

"""
python-multipart==0.0.6

# 1. File
간단히 File 클래스를 생성하고
bytes라고 바이트열임을 명시해주시면 됩니다.

하지만 파일이름이나 이미지등 자세한 정보를 받을 수 없습니다.
그래서 Uploade 파일을 이용합니다.

# 2. UploadFile
UploadFile에는 다양한 정보가 있는데, 재밌는 것은 기존 IO(파이썬 표준 입출력 객체)와 같은 메소드를 비동기로 지원합니다.
그래서 아래와 같은 메소드들을 지원하죠.
- write, read, seek, close

UploadeFile의 경우는 비동기 함수이기 때문에 `await`을 반드시 써줘야합니다.

"""