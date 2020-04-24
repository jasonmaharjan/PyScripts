# Automate chrome browser activities!
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title                                   # Check for existence
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
#print(show_message_button.get_attribute('innerHTML'))                                # Button Text

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')

user_message.clear()
user_message.send_keys('Message!')

show_message_button.click()
output = chrome_browser.find_element_by_id('display')

assert 'Message!' in output.text

message = chrome_browser.find_element_by_css_selector('#get-input > .btn')

# chrome_browser.quit()