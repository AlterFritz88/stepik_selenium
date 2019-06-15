from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()
browser.get(link)

troll_button = browser.find_element_by_css_selector('body > form > div > div > button').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id('input_value').text

input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(x))

button_1 = browser.find_element_by_css_selector('body > form > div > div > button')
button_1.click()
