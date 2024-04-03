import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

dotenv.load_dotenv()
# Fictional
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.DOWN = 0
        self.UP = 0
        # Config
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--window-size=1200,800')
        # Create webdriver
        self.driver = webdriver.Chrome(options)

    def internet_speed(self):
        d = self.driver
        d.get("https://www.speedtest.net/")
        sleep(3.5)
        # privacy button
        d.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        # Start button — Go
        d.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(50)
        # Close popup
        d.find_element(By.XPATH,
                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a').click()
        self.DOWN = d.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.UP = d.find_element(By.CSS_SELECTOR, ".upload-speed").text
        print(f"DOWNLOAD  {self.DOWN} Mbps  |  UPLOAD  {self.UP} Mbps")

    def tweet_a_complain(self):
        if self.DOWN < PROMISED_DOWN or self.UP < PROMISED_UP:
            d = self.driver
            d.get("https://twitter.com/login")
            sleep(3.5)

            email = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div['
                                             '1]/label/div/div[2]/div/input')
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div['
                                                '2]/label/div/div[2]/div/input')
            email.send_keys(os.getenv('TWITTER_EMAIL'))
            password.send_keys(os.getenv('TWITTER_CODE'))
            sleep(2)
            password.send_keys(Keys.ENTER)
            sleep(5)

            tweet_compose = self.driver.find_element(By.XPATH,
                                                     '//*[@id="react-root"]/div/div/div['
                                                     '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                     '1]/div/div/div/div[2]/div['
                                                     '1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
                                                     '2]/div/div/div/div')
            tweet = f"Hey Internet Provider, why is my internet speed {self.DOWN}down/{self.UP}up when I pay for " \
                    f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            sleep(3)

            self.driver.find_element(By.XPATH,
                                     '//*[@id="react-root"]/div/div/div['
                                     '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                     '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()
            sleep(2)
            print('Complain sent')

        else:
            print("All good")


bot = InternetSpeedTwitterBot()
bot.internet_speed()
bot.tweet_a_complain()

# bot.driver.quit()
