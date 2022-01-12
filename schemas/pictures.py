from typing import Optional
from pydantic import BaseModel

class Picture(BaseModel):
    id: Optional[int]
    id_enigma: int
    url: str
    order: int