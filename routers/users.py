from pickle import APPEND
## FastApi

from fastapi import APIRouter
from fastapi import FastAPI, status, Body


from typing import List
import json

## Models
from models.user import User
from models.userRegister import UserRegister

router = APIRouter(
    prefix = "/users",
    tags = [ "Users" ]
)


@router.get(
    path =  "",
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "show all users",
)
async def show_all_users():
    """
    This path operation shows all users in the app

    Parameters:
        

    Returns a json with all the followings keys
         user_id: UUID
         email: Emailstr
         first_name: str
         last_name: str
         birth_date: str
    """
    with open("users.json", "r", encoding = "utf-8") as f:
        results = json.loads(f.read())
        return results


    
@router.post(
    path =  "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a User",
    tags = [ "Users" ]
)
def signup(user: UserRegister = Body(...)):

    """
    Signup User

    This path operation register a user in the app

    Parameters:
        - Request Body Parameter
            - user: UserRegister

    returns a json with the basic user information:
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: str
    """

    with open("users.json", "r+", encoding = "utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user






@router.delete(
    path =  "/{user_id}/delete",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a User",
    tags = [ "Users" ]
)

def delete_a_user():
    pass