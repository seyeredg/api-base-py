from pickle import APPEND


## FastApi

from fastapi import APIRouter
from fastapi import FastAPI, status, Body


from typing import List
import json

## Models
from models.user import User
from models.userRegister import UserRegister