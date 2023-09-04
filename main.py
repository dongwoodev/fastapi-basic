from typing import Optional, List

from pydantic import BaseModel, parse_obj_as
from fastapi import FastAPI, Query, Path
import uvicorn

app = FastAPI()

tracks = (
    {
        "id":1,
        "user_id": 1,
        "singer": "BlackPink",
        "song": "shutdown",
        "love" : 98.0,
        "stream": 2500,
    },
    {
        "id":2,
        "user_id": 1,
        "singer": "BlackPink",
        "song": "Howyoulikethat",
        "love" : 92.0,
        "stream": 3000,
    },
    {
        "id":3,
        "user_id": 1,
        "singer": "BlackPink",
        "song": "휘파람",
        "love" : 94.0,
        "stream": 2000,
    },
)

class Track(BaseModel):
    """
    ## Track 클래스
    - singer
    - song
    - love
    - stream
    """
    singer: str
    song: str
    love: float
    stream: int = 0

@app.get("/users/{user_id}/tracks", response_model=List[Track])
def get_track(
    user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
    # Path(...(alias,생략_여기서는_required를 표현), gt(0보다 큰), )
    song: str = Query(None, min_length=1, max_length=10, title="노래 이름"),
    # Query(1~10)
):
    user_tracks = []
    for track in tracks:
        if track["user_id"] == user_id:
            user_tracks.append(track)
    
    response = []
    for track in tracks:
        if song is None:
            response = user_tracks
            break
        if track["song"] == song:
            response.append(track)
    
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""
# Path, Query로 데이터 검증!
http ':8000/users/1/tracks?song=shutdown'
http ':8000/users/1/tracks?song=휘파람'

"""