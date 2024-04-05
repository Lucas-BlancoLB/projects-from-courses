import os
import dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver, common
from selenium.webdriver.common import by, keys
from time import sleep

dotenv.load_dotenv()

class SFRentingResearch:

    def __init__(self):
        # get response / create soup
        r = requests.get('https://appbrewery.github.io/Zillow-Clone/').text
        self.soup = BeautifulSoup(r, 'html.parser')

        # Config
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--window-size=1200,800')
        # Create webdriver
        self.driver = webdriver.Chrome(options)
        self.scraping_zillow_copy()

    def scraping_zillow_copy(self):
        research_result = [[x.find_next(name='address').text.strip('\n '),
                            x.find_next(class_="PropertyCardWrapper__StyledPriceLine").text.replace('/mo', ''),
                            x.find_next(class_='StyledPropertyCardDataArea-anchor').get('href')]
                           for x in self.soup.find_all(class_='StyledPropertyCard-c11n-8-84')]
        # print(research_result)

        self.filling_google_form(research_result)

    def filling_google_form(self, research_result):
        self.driver.get(os.getenv('GOOGLE_FORM'))
        sleep(5)

        for list_ in research_result:
            # getting input address
            address_input = self.driver.find_elements(by.By.CLASS_NAME, 'whsOnd ')[0]
            price_input = self.driver.find_elements(by.By.CLASS_NAME, 'whsOnd ')[1]
            link_input = self.driver.find_elements(by.By.CLASS_NAME, 'whsOnd ')[2]

            # applying text input
            address_input.send_keys(list_[0])
            price_input.send_keys(list_[1])
            link_input.send_keys(list_[2])

            sleep(2.1)
            link_input.send_keys(keys.Keys.TAB, keys.Keys.ENTER)  # to hit send
            sleep(3.2)
            self.driver.find_element(by.By.CSS_SELECTOR, '.c2gzEf a').click()  # to send a new answer
            sleep(2.5)

        self.driver.quit()


bot = SFRentingResearch()
