import logging
from fastapi import APIRouter, Body, Depends, status

from api.controllers.renting import RentController
from api.schemas.renting import (
    RentReturnSchema,
    RentSchema,
)

logger = logging.getLogger("monitoring")

location_router = APIRouter(prefix="/api/v1")


@location_router.post(
    "/search", status_code=status.HTTP_200_OK, response_model=RentReturnSchema
)
async def search_location(
    renting_data: RentSchema,
    renting_controller=Depends(RentController),
):
    return await renting_controller.search(renting_data)
