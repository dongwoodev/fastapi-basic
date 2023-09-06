"""
### 3. Schemas
Pydantic 모듈을 Models 대신 Schemas라는 말을 사용합니다.

- `Userbase` : email
- `UserCreate` : password

Config : Pydantic이 SQLArchmy 을 사용할 수 있게 합니다.

"""
from pydantic import BaseModel

# email
class UserBase(BaseModel):
    email: str

# password
class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

