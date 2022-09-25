#Python 

from argparse import OPTIONAL
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional
from uuid import UUID
from . import userBase


class userLogin(userBase.UserBase):
        password: str = Field(
        ...,
        min_length = 8
        )