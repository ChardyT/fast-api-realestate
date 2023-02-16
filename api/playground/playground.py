import json
from pathlib import Path
from typing import Any, Dict, List
import pandas as pd
import chardet


class DataFramePlayground:
    def __init__(self):
        pass
    #Play with pandas dataframe to explore data
    def play_with_dataframe_rent_indicator_optimized(self, departement: str) -> List[Dict[str, Any]]: 
    #Data frame from csv
        with open(Path().cwd() / "api" / "scraping" / "indicateurs-loyers-appartements.csv", encoding="ISO-8859-1") as file:
            data = pd.read_csv(file, sep=";")
        
        data = data[data['DEP'] == departement]
        return json.loads(self.dataframe_to_json(data))


    def play_with_dataframe_city_rate_optimized(self, ville: List[str]) -> List[Dict[str, Any]]: 
        #Data frame from csv
        with open(Path().cwd() / "api" / "scraping" / "cities_rate.csv") as file:
            data = pd.read_csv(file, sep=",")
    
            data = data[data['Villes'].isin(ville)]
            print(data)
            return json.loads(self.dataframe_to_json(data))


    #convert dataframe to json in format records [{column -> value}, … , {column -> value}]
    def dataframe_to_json(self,dataframe):
        return dataframe.to_json(orient="records")

    #Detect encoding of a file
    def detect_encoding(self,file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
        return chardet.detect(rawdata)['encoding']

# if __name__ == '__main__':
#     playground = DataFramePlayground()
    # print(playground.detect_encoding("../scraping/indicateurs-loyers-appartements.csv"))
    # playground.play_with_dataframe_rent_indicator("64")
    # playground.play_with_dataframe_city_rate(["Viodos-Abense-de-Bas","Aast","Pau","Abidos","Anglet","Bordeaux"])
    