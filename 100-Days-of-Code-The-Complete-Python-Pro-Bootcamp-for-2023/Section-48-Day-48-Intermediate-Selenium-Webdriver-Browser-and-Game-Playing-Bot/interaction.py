from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# to configurate Chrome to not close when the code ran
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # 'detach' seems to be a chrome thing
options.add_argument('--window-size=1200,800')

# Create and configurate the Chrome webdriver
driver = webdriver.Chrome(options=options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')  # navigate to the page

# Get the number of articles on Wikipedia
articles_num = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(articles_num.text)
# articles_num.click()

# Find an element by LINK_TEXT | click using click()
content_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# content_portals.click()

# Find an element by NAME | text input using send_keys('')
search = driver.find_element(By.NAME, 'search')
search.send_keys("Mirror", Keys.ENTER)

# driver.quit()