import logging
from logging.config import dictConfig
from fastapi import FastAPI
from api.core.log_config import LogConfig

from api.routes.renting import location_router


dictConfig(LogConfig().dict())
logger = logging.getLogger("monitoring")

# FastApi app
app = FastAPI(
        debug=True,
        title="Flat location API docs",
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redocs",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
)


app.include_router(location_router)
