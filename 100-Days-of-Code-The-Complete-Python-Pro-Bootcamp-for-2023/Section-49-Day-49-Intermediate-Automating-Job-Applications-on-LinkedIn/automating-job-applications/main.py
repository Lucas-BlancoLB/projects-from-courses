import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

dotenv.load_dotenv()

# config
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--window-size=1200,800')

# creating webdriver
driver = webdriver.Chrome(options)
driver.get(os.getenv("SITE"))

# Login
login = driver.find_element(By.XPATH, '//*[@id="session_key"]')
login.send_keys(os.getenv("EMAIL"), Keys.TAB, os.getenv("CODE"), Keys.ENTER)

# jobs page
driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div').click()
time.sleep(5)

# jobs application
search = driver.find_element(By.CSS_SELECTOR, ".relative input")
# 1⁰ str — the job's title | 2⁰ str — location
search.send_keys("Python developer", Keys.TAB, Keys.TAB,"Remote", Keys.ENTER)
time.sleep(5)

# Saving applications
applications = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
apply_num, errors_num = 0, 0
# [print(applications.text) for applications in applications[0]]  # first item in the list

for job in applications:
    try:
        job.click()  # job result item
        time.sleep(4)

        driver.find_element(By.CSS_SELECTOR, '.jobs-save-button').click()  # save/saved button
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, ".artdeco-toasts_toasts button").click()  # close popup from save button
        apply_num += 1
    except Exception as error:
        errors_num += 1
        print(error)

print(f"Successfully {apply_num}\nError {errors_num} ")

# driver.quit()