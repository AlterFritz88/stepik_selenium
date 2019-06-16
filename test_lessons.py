from selenium import webdriver

import time
import math

browser = webdriver.Firefox()
browser.implicitly_wait(5)

link = 'https://stepik.org/lesson/236896/step/1'

browser.get(link)
input_1 = browser.find_element_by_tag_name("textarea")
input_1.send_keys(str(math.log(int(time.time()))))

button = browser.find_element_by_class_name('submit-submission ')
button.click()
time.sleep(1)
ans_text = browser.find_element_by_tag_name('pre').text

assert ans_text == 'Correct!'