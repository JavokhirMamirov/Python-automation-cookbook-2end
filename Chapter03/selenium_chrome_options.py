from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--headless")

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://httpbin.org/forms/post")
browser.save_screenshot('screenshot.png')
