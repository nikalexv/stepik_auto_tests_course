from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    x = int(value1.text)

    value2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    y = int(value2.text)

    z = str(x+y)
    print(type(z))

    value3 = Select(browser.find_element(By.TAG_NAME, "select"))
    value3.select_by_value(z)
  
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