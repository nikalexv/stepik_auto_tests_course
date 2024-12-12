from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    y = calc(value1.text)
   
    browser.execute_script("window.scrollBy(0, 100);")
   

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(str(y))

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    #print(y)

    #value2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    #y = int(value2.text)

    #z = str(x+y)
    #print(type(z))

    #value3 = Select(browser.find_element(By.TAG_NAME, "select"))
    #value3.select_by_value(z)
  
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()