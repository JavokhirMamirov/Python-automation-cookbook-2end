from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://httpbin.org/forms/post")


custname = browser.find_element(by='name', value="custname")
custname.clear()
custname.send_keys("Javokhir Mamirov")

for size_element in browser.find_elements(by='name', value='size'):
    if size_element.get_attribute('value') == 'medium':
        size_element.click()

for topping in browser.find_elements('name','topping'):
    if topping.get_attribute('value') in ['bacon', 'cheese']:
        topping.click()

browser.find_element(by=By.TAG_NAME, value='form').submit()

browser.quit()