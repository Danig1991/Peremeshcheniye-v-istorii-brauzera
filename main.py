import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# ввод логина/пароля, нажатие на кнопку Login
driver_chrome.find_element(By.ID, "user-name").send_keys("standard_user")
driver_chrome.find_element(By.ID, "password").send_keys("secret_sauce")

# пауза 1 секунда
time.sleep(1)

driver_chrome.find_element(By.ID, "login-button").click()
print("Успешная авторизация.")

# добавить в корзину продукт
driver_chrome.find_element(
    By.XPATH,
    "//button[@id='add-to-cart-sauce-labs-backpack']"
).click()
print("Продукт добавлен в корзину.")

# пауза 1 секунда
time.sleep(1)

# перейти в корзину
driver_chrome.find_element(By.ID, "shopping_cart_container").click()
print("Переход в корзину.")

# пауза 1 секунда
time.sleep(1)

# вернуться на страницу каталога при помощи кнопки браузера
driver_chrome.back()
print("Возвращение в каталог.")

# пауза 1 секунда
time.sleep(1)

# вернуться в корзину при помощи кнопки браузера
driver_chrome.forward()
print("Возвращение в корзину.")

# пауза 2,5 секунды
time.sleep(2.5)

# закрыть окно браузера
driver_chrome.close()
print("Закрытие окна.")
