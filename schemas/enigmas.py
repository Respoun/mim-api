from typing import Optional
from pydantic import BaseModel

class Enigma(BaseModel):
    id: Optional[int]
    id_quest: int
    title: str
    id_previous: int
    id_next: int
    content: str
    response: str
    indice: str