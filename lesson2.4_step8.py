from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button = WebDriverWait(browser, 11).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    y = calc(x)

    option1 = browser.find_element(By.NAME, "text")
    option1.send_keys(y)

    button1 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()