#Python 

from argparse import OPTIONAL
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional
from uuid import UUID
from . import userBase


class User(userBase.UserBase):
    
    first_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    last_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    birth_date: Optional[date] = Field(default = None)


if __name__ == '__main__':
    User = User()