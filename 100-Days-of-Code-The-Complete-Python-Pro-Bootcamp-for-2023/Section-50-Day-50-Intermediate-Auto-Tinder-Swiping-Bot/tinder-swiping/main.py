import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

dotenv.load_dotenv()

# config webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--window-size=1200,800')

# creating webdriver
driver = webdriver.Chrome(options)
driver.get('http://www.tinder.com/')
root_window = driver.window_handles[0]
time.sleep(5)

# login
driver.find_element(By.XPATH,
'//*[@id="t425926696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()
time.sleep(1.5)
driver.find_element(By.XPATH,
'//*[@id="t-1302454380"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
time.sleep(2)
# facebook inputs
facebook_popup = driver.window_handles[1]
driver.switch_to.window(facebook_popup)
login = driver.find_element(By.XPATH, '//*[@id="email"]')
login.send_keys(os.getenv("FACEBOOK_EMAIL"), Keys.TAB, os.getenv("FACEBOOK_PASS"), Keys.ENTER)

driver.switch_to.window(root_window)
time.sleep(5)

# 100 likes - free tier
for i in range(100):
    try:
        driver.find_element(By.XPATH,
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
        time.sleep(1)
    # selenium error handling
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a').click()

        except NoSuchElementException:
            time.sleep(1)

# driver.quit()
