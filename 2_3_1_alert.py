from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    input1 = browser.find_element(By.CSS_SELECTOR, "button")
    input1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    y = calc(value1.text)

    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input2.send_keys(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()