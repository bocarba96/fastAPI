from fastapi import FastAPI, HTTPException
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from model import User, Gender, Role

app = FastAPI()


db: List[User] = [
    User(id=uuid4(), first_name="Bocar", last_name="BA", gender=Gender.male, roles=[Role.user])
]


@app.get("/hello")
async def root():
    return {
        "message": "Bienvenue sur fastApi"
    }

@app.get("/api/v1/users")
async def get_users():
    return db


@app.get("/api/v1/users/{user_id}")
async def get_users(user_id: str):
    for user in db:
        if (str(user.id) == user_id):
            return user
        raise HTTPException(
            status_code=404,
            detail=f"User with id = {user_id} not found"
        )
    return {
        "message":"Aucun user dans la base de donnee"
    }

@app.post("/api/v1/users")
async def post_users(user: User):
    db.append(user);
    raise HTTPException(
        status_code=200,
        detail="OK"
    )
 