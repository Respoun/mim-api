from fastapi import FastAPI
from routes.quests import router as quest
from routes.pictures import router as picture
from routes.enigmas import router as enigma
from config.openapi import tags_metadata

app = FastAPI(
    title="Mim API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(quest)
app.include_router(picture)
app.include_router(enigma)
