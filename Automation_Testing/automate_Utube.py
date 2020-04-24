# Youtube Automation: 
# Give the keyword to search
# Filter @ view count
# Play the first video
 
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

search_query = sys.argv[1]

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

wait = WebDriverWait(browser, 5)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

browser.get('https://www.youtube.com')
# browser.execute_script("window.open('','_blank');")

# Type and Search 
wait.until(presence((By.CSS_SELECTOR, 'ytd-searchbox')))
browser.find_element_by_css_selector('ytd-searchbox').send_keys(search_query)
browser.find_element_by_id('search-icon-legacy').click()    # Alternative: .send_keys(Keys.RETURN)

# Press Filter Button
Filter_button_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/paper-button/yt-icon'
wait.until(presence((By.XPATH, Filter_button_xpath)))
browser.find_element_by_xpath(Filter_button_xpath).click()

# Filter: View Count
Filter_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string'
wait.until(visible((By.XPATH, Filter_xpath)))
browser.find_element_by_xpath(Filter_xpath).click()

# Play first video
First_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/div[2]'
wait.until(visible((By.XPATH, First_xpath )))
browser.find_element_by_xpath(First_xpath).click()


# Automate playing video directly through URL
'''
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 5)
visible = EC.visibility_of_element_located

video_query = 'Bohemien+Rhapsody'

# Append video to URL
driver.get("https://www.youtube.com/results?search_query=" + str(video_query))

# play video
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()
'''