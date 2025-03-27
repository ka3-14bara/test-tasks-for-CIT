from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Режим без графики
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome()
driver.get("https://www.arealme.com/colors/ru/")

start_button = (driver.find_element(By.ID, "start"))
start_button.click()

options.page_load_strategy = 'eager'
try:
    while True:
        #time.sleep(0.01)
        area = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "div[style*='background-color: rgb(221, 221, 221)'] span")
            )
        )

        colors =[]
        n1 = 0
        for i in range(len(area)):
            color = area[i].value_of_css_property('background-color')
            if len(colors) == 4 and i > 3:
                break
            if color not in colors:
                colors.append(color)
                colors.append(i)
            elif color == colors[0]:
                n1 += 1
        if n1 == 0:     
            area[colors[1]].click()
        else:
            area[colors[3]].click()
except:
    time.sleep(15)
finally:
    driver.quit()