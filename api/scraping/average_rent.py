import requests
from bs4 import BeautifulSoup
import pandas as pd



def get_average_rent_file_url():
    response = requests.get('https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2018/')
    soup = BeautifulSoup ( response.content , "html.parser" )
    average_rent_downlaod_file_url=soup.find('a',class_="fr-btn fr-btn--sm fr-icon-download-line").get('href')
    print(average_rent_downlaod_file_url)
    return average_rent_downlaod_file_url


def download_file(url):
    req = requests.get(url)
    url_content = req.content
    csv_file = open('average_rent.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    print(csv_file)
    return csv_file


def get_average_rent_cities_by_insee(code_insee):
    data = pd.read_csv("average_rent.csv",encoding='latin-1')

    for index, row in data.iterrows():
        print(index,'===========>>>>>>',row)
        print()
        if row['DEP']==code_insee:
            print(row['LIBGEO'],row['loypredm2'], row['lwr.IPm2'],row['upr.IPm2'])


# if __name__ == '__main__':
#     file_url=get_average_rent_file_url()
#     csv_file=download_file(file_url)
#     get_average_rent_cities_by_insee(64)
