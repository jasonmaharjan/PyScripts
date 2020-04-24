from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')

browser.maximize_window()
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

value_a = browser.find_element_by_id('sum1')
value_b = browser.find_element_by_id('sum2')

value_a.clear()
value_a.send_keys('1')

value_b.clear()
value_b.send_keys('2')

button = browser.find_element_by_css_selector('#gettotal > .btn')
button.click()

output = browser.find_element_by_id('displayvalue')
print(output.text)

