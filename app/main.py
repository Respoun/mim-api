from fastapi import FastAPI
from .src.routes.quests import router as quest
from .src.routes.pictures import router as picture
from .src.routes.enigmas import router as enigma
from .src.routes.health import router as health
from .config.openapi import tags_metadata
from fastapi_simple_security import api_key_router
import os

secret = os.getenv("FASTAPI_SIMPLE_SECURITY_SECRET")

app = FastAPI(
    title="Mim API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(quest)
app.include_router(picture)
app.include_router(enigma)
app.include_router(health)
app.include_router(api_key_router, prefix="/auth", tags=["_auth"])