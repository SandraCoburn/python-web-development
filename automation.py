#pip install selenium in venv
# Get chrome drive and add it to project folder

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
# chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/')
print('Python Easy Demo' in chrome_browser.title) # false -> checks for string in title

button_text = chrome_browser.find_element_by_class_name('btn btn-default')
print(button_text.get_attribute('innerHTMl'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys(("I'm cool!"))




