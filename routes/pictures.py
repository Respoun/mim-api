from fastapi import APIRouter
from config.db import conn
from models.pictures import pictures
from schemas.pictures import Picture
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

router = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@router.get(
    "/pictures",
    tags=["pictures"],
    response_model=List[Picture],
    description="Get a list of all pictures",
)
def get_quests():
    return conn.execute(pictures.select()).fetchall()

@router.get(
    "/pictures/{id}",
    tags=["pictures"],
    response_model=Picture,
    description="Get a single picture by Id",
)
def get_pictures(id: str):
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()


@router.post("/", tags=["pictures"], response_model=Picture, description="Create a new picture")
def create_pictures(picture: Picture):
    new_picture = {"id_enigma": picture.id_enigma, "url": picture.url, "order": picture.order}
    result = conn.execute(pictures.insert().values(new_picture))
    return conn.execute(pictures.select().where(pictures.c.id == result.lastrowid)).first()


@router.put(
    "pictures/{id}", tags=["pictures"], response_model=Picture, description="Update a picture by Id"
)
def update_quest(picture: Picture, id: int):
    conn.execute(
        pictures.update()
        .values(id_enigma=picture.id_enigma, url=picture.url, order=picture.order)
        .where(pictures.c.id == id)
    )
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()


@router.delete("/{id}", tags=["pictures"], status_code=HTTP_204_NO_CONTENT)
def delete_quest(id: int):
    conn.execute(pictures.delete().where(pictures.c.id == id))
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()
