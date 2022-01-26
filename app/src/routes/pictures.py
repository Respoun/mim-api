from fastapi import APIRouter, Depends
from app.config.db import conn
from app.src.models.pictures import pictures
from app.src.schemas.pictures import Picture
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from fastapi_simple_security import api_key_security
from cryptography.fernet import Fernet

router = APIRouter(
    prefix="/pictures",
    tags=["pictures"],
    responses={404: {"description": "Not found"}},
)


key = Fernet.generate_key()
f = Fernet(key)


@router.get(
    "",
    dependencies=[Depends(api_key_security)],
    response_model=List[Picture],
    description="Get a list of all pictures",
)
def get_pictures():
    return conn.execute(pictures.select()).fetchall()

@router.get(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    response_model=Picture,
    description="Get a single picture by Id",
)
def get_pictures(id: str):
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()


@router.post(
    "",
    dependencies=[Depends(api_key_security)], 
    response_model=Picture, 
    description="Create a new picture")
def create_pictures(picture: Picture):
    new_picture = {"id_enigma": picture.id_enigma, "url": picture.url, "order": picture.order}
    result = conn.execute(pictures.insert().values(new_picture))
    return conn.execute(pictures.select().where(pictures.c.id == result.lastrowid)).first()


@router.put(
    "/{id}",
    dependencies=[Depends(api_key_security)], 
    response_model=Picture, 
    description="Update a picture by Id"
)
def update_pictures(picture: Picture, id: int):
    conn.execute(
        pictures.update()
        .values(id_enigma=picture.id_enigma, url=picture.url, order=picture.order)
        .where(pictures.c.id == id)
    )
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()


@router.delete(
    "/{id}",
    dependencies=[Depends(api_key_security)], 
    status_code=HTTP_204_NO_CONTENT)
def delete_pictures(id: int):
    conn.execute(pictures.delete().where(pictures.c.id == id))
    return conn.execute(pictures.select().where(pictures.c.id == id)).first()
