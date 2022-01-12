from fastapi import APIRouter
from config.db import conn
from models.quests import quests
from schemas.quests import Quest
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

router = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)


@router.get(
    "/quests",
    tags=["quests"],
    response_model=List[Quest],
    description="Get a list of all quests",
)
def get_quests():
    return conn.execute(quests.select()).fetchall()

@router.get(
    "/quests/{id}",
    tags=["quests"],
    response_model=Quest,
    description="Get a single quest by Id",
)
def get_quests(id: str):
    return conn.execute(quests.select().where(quests.c.id == id)).first()


@router.post("/", tags=["quests"], response_model=Quest, description="Create a new quest")
def create_quest(quest: Quest):
    new_quest = {"title": quest.title}
    result = conn.execute(quests.insert().values(new_quest))
    return conn.execute(quests.select().where(quests.c.id == result.lastrowid)).first()


@router.put(
    "quests/{id}", tags=["quests"], response_model=Quest, description="Update a quest by Id"
)
def update_quest(user: Quest, id: int):
    conn.execute(
        quests.update()
        .values(title=quest.title)
        .where(quests.c.id == id)
    )
    return conn.execute(quests.select().where(quests.c.id == id)).first()


@router.delete("/{id}", tags=["quests"], status_code=HTTP_204_NO_CONTENT)
def delete_quest(id: int):
    conn.execute(quests.delete().where(quests.c.id == id))
    return conn.execute(quests.select().where(quests.c.id == id)).first()
