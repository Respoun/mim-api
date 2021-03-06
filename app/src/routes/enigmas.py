from fastapi import APIRouter, Depends
from app.config.db import conn
from app.src.models.enigmas import enigmas
from app.src.schemas.enigmas import Enigma
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet
from fastapi_simple_security import api_key_security

router = APIRouter(
    prefix="/enigmas",
    tags=["enigmas"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)

@router.get(
    "",
    dependencies=[Depends(api_key_security)],
    response_model=List[Enigma],
    description="Get a list of all enigmas",
)
def get_enigmas():
    return conn.execute(enigmas.select()).fetchall()

@router.get(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    response_model=Enigma,
    description="Get a single enigma by Id",
)
def get_enigmas(id: str):
    return conn.execute(enigmas.select().where(enigmas.c.id == id)).first()


@router.post(
    "",
    dependencies=[Depends(api_key_security)], 
    response_model=Enigma, 
    description="Create a new Enigma")
def create_enigma(enigma: Enigma):
    new_enigma = {"id_quest": enigma.id_quest, "title": enigma.title, "id_previous": enigma.id_previous, 
                 "id_next": enigma.id_next,"content": enigma.content, "response": enigma.response, "indice": enigma.indice}
    result = conn.execute(enigmas.insert().values(new_enigma))
    return conn.execute(enigmas.select().where(enigmas.c.id == result.lastrowid)).first()


@router.put(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    response_model=Enigma, 
    description="Update a Enigma by Id"
)
def update_enigma(enigma: Enigma, id: int):
    conn.execute(
        enigmas.update()
        .values(id_enigma=enigma.id_enigma, url=enigma.url, order=enigma.order)
        .where(enigmas.c.id == id)
    )
    return conn.execute(enigmas.select().where(enigmas.c.id == id)).first()


@router.delete(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    status_code=HTTP_204_NO_CONTENT
)
def delete_enigma(id: int):
    conn.execute(enigmas.delete().where(enigmas.c.id == id))
    return conn.execute(enigmas.select().where(enigmas.c.id == id)).first()
