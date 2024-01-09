from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()

# test otomasyonu
# test: beklentileri karşılıyor mu=
# 1. istenileni yapıyor mu? pozitif test 2. istenmeyeni yapıyor mu negatif

# internet login sayfasına git  https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")
# kullanıcı adi gir
username = driver.find_element(By.ID, "username")
username.send_keys("test")
# şifre gir
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

    # log in düğmesine tıkla
    # yanlış kullanıcı adı : Your username is invalid!
driver.find_element(By.CLASS_NAME, "radius").click()
message = driver.find_element(By.ID, "flash").text

if "Your username is invalid!" in message:
    print("OK, yanlış kullanıcı adi doğru çalışıyor")
else:
    print("Hata: yanlış kullanıcı adı çalışmıyor")

    # yanlış şifre : Your password is invalid!
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("test")
driver.find_element(By.CLASS_NAME, "radius").click()
message = driver.find_element(By.ID, "flash").text

if "Your password is invalid!" in message:
    print("OK, yanlış şifre doğru çalışıyor")
else:
    print("Hata: yanlış şifre çalışmıyor")

    # ikisi de doğru ise mesaj : You logged into a secure area! link : secure içerecek sayfa başlığı : Secure Area
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
message = driver.find_element(By.ID, "flash").text
if "You logged into a secure area!" in message:
    print("OK, Giriş tamamlandı ve secure sayfasına ulaşıldı!")
else:
    print("Hata : Giriş başarısız")

link = driver.current_url
if "secure" in link:
    print("OK, link secure içeriyor")
else:
    print("HATA : link secure içermiyor")

dogru_mesaj = driver.find_element(By.CLASS_NAME, "subheader").text
print(" Mesaj : " + dogru_mesaj)

# Logout düğmesine tıklayacak
driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()
link = driver.current_url

#Linki doğrulayacak
if "login" in link:
    print("OK, link login")
else:
    print("hata")


# Aynı kodları defalarca yazmamak için giriş işlemi username ve password bilgileri ile fonksiyon ile yapılabilir.
def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "radius").click()
    message = driver.find_element(By.ID, "flash").text
    return message

mesaj = login("tomsmith", "SuperSecretPassword!")

if "You logged into a secure area!" in mesaj:
    print("2. defa fonksiyon ile doğru çalıştırıldı")
else:
    print("2. defa fonksiyon ile çalıştırmada hata var!")
driver.quit()