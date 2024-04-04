# I didn't do day 52 to avoid getting annoyed and banned, so I read and followed through other solutions to understand how to solve this challenge. I went through searching for the things that I didn't understand.

# I learned about //tag, contains(), text(), and 'piece of a str':
# //tag: searches through the whole document for the specified tag.
# contains(): looks for what's inside that specific tag.
# text(): indicates that I'm looking for text.
# 'piece of a str': searches for this specific text.

# For example:
self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")

# --------------

# I learned about arguments[0], arguments[0].scrollTop, and arguments[0].scrollHeight used to perform scroll motion.
# arguments[0]: represents the element to be used in the JavaScript code — [0] <- the index refers to the modal (it's the first and only argument im my case).
# arguments[0].scrollTop: retrieves the current position of the scroll in the page or element.
# arguments[0].scrollHeight: retrieves the height of the scroll.

# For example:
modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
