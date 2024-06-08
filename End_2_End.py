from selenium import webdriver # управляет браузером
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time ## управляем временем


driver = webdriver.Chrome(service=Service())
driver.set_window_size(1024,768)
print('TC-1: Вход с валидными данными')

try:
    driver.get('https://idemo.bspb.ru/')
    username = driver.find_element(By.ID,"username")
    username.clear()
    username.send_keys('demo')
    password = driver.find_element(By.NAME,"password")
    password.clear()
    password.send_keys('demo')

    time.sleep(2) ## добавляем паузу

    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.ID,"login-otp-button").click()

    if driver.find_element(By.ID,"user-avatar"):print("TC-1 FINISHED")
    print("\033[92m{}\033[0m".format("TEST PASS"))
    driver.save_screenshot("TC1_PASSED.png")

    driver.find_element(By.ID,"logout-button").click() ## разлогин

except:
    driver.save_screenshot("TC1_FAILED.png")
    print("TC-1 FINISHED")
    print("\033[31m{}\033[0m".format("TEST FAIL"))

time.sleep(5) ## добавляем паузу

print('TC-2: Запрет входа с невалидными данными')

## driver.delete_cookie()

import string
import random

rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
# для разнообразия отдельная переменная другого формата,
# но для негативного сценария не имеет значения
rand_password = ''.join(random.choice(string.ascii_uppercase) for i in range(12))
try:
    driver.get('https://idemo.bspb.ru/')
    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys(rand_string)
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(rand_password)

    driver.find_element(By.ID, "login-button").click()

    if driver.find_element(By.ID, "login-button"):print("TC-2 FINISHED")
    print("\033[92m{}\033[0m".format("TEST PASS"))
    driver.save_screenshot("TC2_PASSED.png")
except:
    driver.save_screenshot("TC2_FAILED.png")
    print("TC-2 FINISHED")
    print("\033[31m{}\033[0m".format("TEST FAIL"))

## боремся с утечкой памяти
    driver.quit()