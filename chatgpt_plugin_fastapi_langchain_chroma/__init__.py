from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routers.well_known import well_known
from routers.quote import quote
from .config import settings


def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(well_known)
    app.include_router(quote, prefix="/api")
    app.mount("/", StaticFiles(directory="public", html=True))
    return app
