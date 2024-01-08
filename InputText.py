
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://www.google.com")

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("selenium")
searchbox.send_keys(Keys.ENTER)
