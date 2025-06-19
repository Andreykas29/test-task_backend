from fastapi import FastAPI
from app.db import engine, Base
from app.models import cat
from app.api.cat import router as cat_router
from app.api.mission import router as mission_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



Base.metadata.create_all(bind=engine)

app.include_router(cat_router, prefix="/cats", tags=["Cats"])
app.include_router(mission_router, prefix="/mission", tags=["Mission"])