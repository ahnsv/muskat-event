from fastapi import FastAPI
from app.infrastructure.presentation.fastapi.router import router

app = FastAPI()
app.include_router(router=router)
