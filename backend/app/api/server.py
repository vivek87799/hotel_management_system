from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.db.database import db


title = "LIMEHOME - Hotel Management system"
description = "Backend api for Hotel Management System"
version = 0.1

def get_application() -> FastAPI():
    app = FastAPI(title=title, description=description, version=version)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    return app

app = get_application()
