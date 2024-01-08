

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://www.apple.com")
link = driver.current_url
baslik = driver.title
print("Sayfa başlığı : " + baslik)
if "apple.com" in link:
    print("Doğru apple sayfasındayız  : "+ link)
driver.maximize_window()
driver.get("http://www.etsy.com")
link = driver.current_url
baslik = driver.title
print("Sayfa başlığı" + baslik)
if "etsy.com" in link:
    print("Doğru etsy sayfasındayız : " +link)
driver.back()
baslik = driver.title
driver.save_screenshot("./screenshot.png")
if "Apple" in baslik:
    print("Tebrikler apple sayfasına döndün")
# şuanki pencereyi kapatır
driver.close()

# driver.quit() - seleniumun kullandığı tüm sekmeleri kapatır