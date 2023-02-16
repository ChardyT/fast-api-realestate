import logging
from fastapi import Depends

from api.schemas.renting import RentReturnSchema, RentSchema
from api.services.rent import RentService

logger = logging.getLogger("monitoring")

class RentController:
    def __init__(
        self,
        renting_service : RentService = Depends(RentService),
    ):
        self.renting_service: RentService = renting_service

    async def search(self, renting_data: RentSchema) -> RentReturnSchema:
        logger.info(renting_data)
        print(renting_data)
        renting_data = renting_data.dict()
        rent_repositories =  await self.renting_service.search_location_optimization(renting_data)
        rent = [repository for repository in rent_repositories]

        return {"rentSchema": renting_data, "cities": rent}
