from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    
    button1.click()

    value1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    y = calc(value1.text)

    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input2.send_keys(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
