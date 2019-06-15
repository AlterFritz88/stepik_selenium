from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Firefox()
browser.get(link)

button = browser.find_element_by_css_selector('body > form > div > div > button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(0.2)

x = browser.find_element_by_id('input_value').text

input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(x))

button_1 = browser.find_element_by_css_selector('body > form > div > div > button')
button_1.click()