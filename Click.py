
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Duckduckgo.com sitesine gider arama kutusuna selenium yazar ve arama buttonuna tıklar ve ardından çıkan sonuçta ilk adrese tıklar
# click() kullanılamayacak zamanlarda Enter'kullanılır.

driver.get("http://www.duckduckgo.com")
driver.maximize_window()
searchbox = driver.find_element(By.ID, "searchbox_input")
searchbox.send_keys("selenium")
driver.find_element(By.CLASS_NAME, "searchbox_searchButton__F5Bwq").click()
driver.find_element(By.ID, "r1-0").click()