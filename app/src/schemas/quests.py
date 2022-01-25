from typing import Optional
from pydantic import BaseModel

class Quest(BaseModel):
    id: Optional[int]
    title: str