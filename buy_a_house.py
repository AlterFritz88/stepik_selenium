from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR'))
button = browser.find_element_by_id('book').click()


x = browser.find_element_by_id('input_value').text

input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(x))

button_1 = browser.find_element_by_id('solve')
button_1.click()

