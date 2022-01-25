from fastapi import APIRouter, Depends
from config.db import conn
from src.models.quests import quests
from src.schemas.quests import Quest
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from fastapi_simple_security import api_key_security

from cryptography.fernet import Fernet

router = APIRouter(
    prefix="/quests",
    tags=["quests"],
    responses={404: {"description": "Not found"}},
)

key = Fernet.generate_key()
f = Fernet(key)


@router.get(
    "",
    dependencies=[Depends(api_key_security)],
    tags=["quests"],
    response_model=List[Quest],
    description="Get a list of all quests",
)
def get_quests():
    return conn.execute(quests.select()).fetchall()

@router.get(
    "/{id}",
    tags=["quests"],
    response_model=Quest,
    description="Get a single quest by Id",
)
def get_quests(id: str):
    return conn.execute(quests.select().where(quests.c.id == id)).first()


@router.post("", response_model=Quest, description="Create a new quest")
def create_quest(quest: Quest):
    new_quest = {"title": quest.title}
    result = conn.execute(quests.insert().values(new_quest))
    return conn.execute(quests.select().where(quests.c.id == result.lastrowid)).first()


@router.put(
    "/{id}", response_model=Quest, description="Update a quest by Id"
)
def update_quest(quest: Quest, id: int):
    conn.execute(
        quests.update()
        .values(title=quest.title)
        .where(quests.c.id == id)
    )
    return conn.execute(quests.select().where(quests.c.id == id)).first()


@router.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_quest(id: int):
    conn.execute(quests.delete().where(quests.c.id == id))
    return conn.execute(quests.select().where(quests.c.id == id)).first()
