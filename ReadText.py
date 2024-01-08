
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Wikipedia anasayfasına gider ve haftanın seçkin maddesi alanındaki yazıyı alır ve konsola yazdırır.

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
vikiText1 = driver.find_element(By.ID, "mp-tfa")
vikiString = vikiText1.text

# gelen yazı alanının ilk kelimesini alma!
vikiString = vikiString.split(",")[0]

print("Seçkin Madde : " + vikiString)

vikiText2 = driver.find_element(By.ID, "mf-tfp")
vikiString2 = vikiText2.text
vikiString2 = vikiString2.split(",")[0]
print("Günün Kaliteli Maddesi : " + vikiString2)
driver.quit()
