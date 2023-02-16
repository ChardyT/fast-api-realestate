import ast
import asyncio
import json
import aiohttp

from typing import List
from fastapi import Depends
import numpy as np
from api.entities.city import City
from api.entities.note import Note
from api.entities.rent import Rent
from api.repositories.city import RentRepository

class RentService:
    def __init__(self, rent_repository: RentRepository = Depends(RentRepository)):
        self.rent_repository: RentRepository = rent_repository
        self.base_url = "https://geo.api.gouv.fr/communes/"
        self.headers = {"Content-Type": "application/json"}
    
    #get every city note in a departement
    async def get_city_note(self, *city_names: List[str]) -> List[Note]:
        try:
            notes = await self.rent_repository.get_city_note(city_names)
            note_data = []
            for note in notes:
                for city in city_names:
                    if city == note["Villes"]:
                        note_data.append(Note(
                            note["Villes"],
                            note["Notes"]
                        ))
                    else:
                        note_data.append(Note(
                            city,
                            0.0
                        ))

            return note_data
        except Exception as e:
            print(e)
            
            
    #get average city average rent in a departement
    async def get_avg_rent_by_dep(self, dep: int) -> list:
        data = await self.rent_repository.get_cities_by_dep(dep)
        result_list: list = []
        for n in range(len(data)):
           result_list.append(Rent(data[n]["id_zone"], data[n]["INSEE"], data[n]["LIBGEO"], data[n]["DEP"], data[n]["loypredm2"]))
        return result_list

    
    
    async def get_city_info_by_insee_optimized(self, *insee: List[str]):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = [session.get(self.base_url + insee_item) for insee_item in insee]
            responses = await asyncio.gather(*tasks)
            return [await r.text() for r in responses]


    async def search_location_optimization(self, renting_data: dict) -> list:
        cities = await self.get_avg_rent_by_dep(renting_data['dep'])
        city_names = [city.ville for city in cities]
        insee_codes = [city.insee for city in cities]
        
        # Execute get_city_note() and get_city_info_by_insee() in parallel
        notes, infos = await asyncio.gather(
            self.get_city_note(*city_names),
            self.get_city_info_by_insee_optimized(*insee_codes)
        ) 
        

        infos = list(map(lambda x: x.replace('Not Found', '{"nom":"NaN","code":"NaN","codeDepartement":"NaN","siren":"NaN","codeEpci":"NaN","codeRegion":"NaN","codesPostaux":["NaN"],"population":0}'), infos))
        # convert infos to a list of dictionaries
        infos = json.loads(json.dumps([json.loads(JSON_STRING) for JSON_STRING in infos]))


        print("=====================================")
        print(infos)
        
        # Extract relevant information from infos
        codes_postaux = [info["codesPostaux"][0] for info in infos]
        population = [info["population"] for info in infos]

        # Create a new list of City objects using list comprehension
        city_list = [
            City(city.avg_rent, note.rate, city.ville, code_postal, pop)
            for city, note, code_postal, pop in zip(cities, notes, codes_postaux, population)
        ]

        return city_list
