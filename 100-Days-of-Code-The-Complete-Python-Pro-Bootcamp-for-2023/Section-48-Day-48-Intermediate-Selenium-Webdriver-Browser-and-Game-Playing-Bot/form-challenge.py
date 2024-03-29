from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# config webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--window-size=1200,800')

# create webdriver with config / get url
drive = webdriver.Chrome(options)
drive.get("http://secure-retreat-92358.herokuapp.com/")  # not a real form it seems

# find form & first text-input
text_inputs = drive.find_elements(By.TAG_NAME, 'input')
print(text_inputs)

text_inputs[0].send_keys('YOUR NAME')
text_inputs[1].send_keys('YOUR LAST NAME')
text_inputs[2].send_keys('YOUR@EMAIL', Keys.TAB, Keys.ENTER)
