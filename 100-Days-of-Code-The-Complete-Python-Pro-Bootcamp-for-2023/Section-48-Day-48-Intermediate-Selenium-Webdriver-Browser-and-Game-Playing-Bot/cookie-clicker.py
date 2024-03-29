from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timer = 1 * 30

# config webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--window-size=1200,800')

# create and get webdriver
driver = webdriver.Chrome(options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')  # Find the cookie
while True:
    start_time = time.time()
    while True:
        cookie.click()

        elapsed_time = time.time() - start_time
        if elapsed_time >= timer:
            break
    money = driver.find_element(By.ID, 'money').text.replace(',', '')  # get the money n edit
    items_to_buy = [[x.text.replace(',', '').split(' ')[-1], x] for x
                    in driver.find_elements(By.CSS_SELECTOR, "#store b")]  # items in store
    # print(items_to_buy)

    # filter items '' and more that i cant pay for
    max_affordable_item = [item for item in items_to_buy if not item[0] == '' and int(item[0]) <= int(money)]
    # print(max_affordable_item)
    if max_affordable_item:
        max_affordable_item[-1][1].click()  # [-1] to get the higher item
