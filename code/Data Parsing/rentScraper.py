import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self):
        # website to scrape
        self.url = 'https://www.rentcafe.com/' 
        
        # empty list to store data
        self.data = []

        # list of cities and states
        self.uscities = pd.read_csv("C:/Users/kleib/Code/kleibo/Projects/Rent-Heat-Map/data/uscities.csv")

    def webScrape(self):
        state_abrv = self.uscities['state_id']
        city = self.uscities['city_ascii']
        city = city.str.replace(" ", "-")

        # Vectorization
        web_path = (state_abrv + '/' + city).to_list()

        print(web_path)
        # # for i in web_path:
        # #     make a request to the website
        # #     response = requests.get(self.url + 'average-rentmarket-trends/us/' + str(i))

        # #     print(response)

        # #     parse the HTML
        # #     soup = BeautifulSoup(response.text, 'html.parser')

test = Scraper()
test.webScrape()

    