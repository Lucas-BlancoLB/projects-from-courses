import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

dotenv.load_dotenv()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)  # To stop closing the browser.

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=os.getenv('URL2'))

# upcoming_events = [element.text.replace('\n', '  ') for element
#                    in driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")]

# upcoming_events = [{'time': element.get_attribute("time"), 'name': element.get_attribute("name")} for element
#                    in driver.find_elements(By.CLASS_NAME, value=".event-widget")]
upcoming_events = [{'time': time.text, 'event': event.text} for time, event in
                   zip(driver.find_elements(By.CSS_SELECTOR, '.event-widget time'),
                       driver.find_elements(By.CSS_SELECTOR, '.event-widget li a'))]
print(upcoming_events)

driver.quit()

# driver.get(url=os.getenv('URL2'))
#
# search_bar = driver.find_element(By.NAME, value='q')  # By NAME
# print(search_bar.get_attribute("placeholder"))
#
# button_go = driver.find_element(By.ID, value="submit")  # By ID
# print(button_go.size)
#
# documentation_a_href = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")  # BY CSS_SELECTOR
# print(documentation_a_href.text)
#
# bug_link_txt = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')  # By XPATH
# print(bug_link_txt.text)
#
#
# driver.quit()


# driver = webdriver.Chrome(options=chrome_option)
#
# driver.get(os.getenv("URL"))
#
# var = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"The price is {var.text}.")
#
# # driver.close()  # close the tab | quit one
# driver.quit()  # Quit the browser | quit everything
