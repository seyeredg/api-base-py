from pickle import APPEND
from fastapi import FastAPI, status, Body
from typing import List
import json
from models.user import User
from models.userRegister import UserRegister

from routers import users


app = FastAPI()


app.include_router(users.router)



