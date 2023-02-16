import asyncio
from typing import List
from fastapi import Depends
from api.playground.playground import DataFramePlayground


class RentRepository:
    def __init__(self, data_frame_play : DataFramePlayground = Depends(DataFramePlayground)):
        self.data_frame_play: DataFramePlayground = data_frame_play
        
    
    async def get_cities_by_dep(self, departement: int):
        cities = self.data_frame_play.play_with_dataframe_rent_indicator_optimized(str(departement))
        return cities

    async def get_city_note(self, city_names: List[str]) -> list:
        note = self.data_frame_play.play_with_dataframe_city_rate_optimized(city_names)
        return note


    
