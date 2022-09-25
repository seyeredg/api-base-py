#Python 

from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

if __name__ == '__main__':
    UserBase = UserBase()