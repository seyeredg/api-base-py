#Python 

from argparse import OPTIONAL
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional
from uuid import UUID
from . import user


class UserRegister(user.User):

    password: str = Field(
    ...,
    min_length = 8,
    max_length=64
    )


if __name__ == '__main__':
    UserRegister = UserRegister()