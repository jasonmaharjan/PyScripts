# Automate Reddit 

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Take user input
search_input = sys.argv[1]

# Notification options in Chrome
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# 1 to allow and 2 to block notifications
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

browser = webdriver.Chrome(options=option, executable_path='./chromedriver')
browser.maximize_window()
browser.get("https://www.reddit.com/search/?q=" + str(search_input)+"&type=link&sort=new")

wait = WebDriverWait(browser, 5)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Open new tab
browser.execute_script("window.open(arguments[0])", "https://www.reddit.com/search/")

