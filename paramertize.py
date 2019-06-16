from selenium import webdriver
import pytest

import time
import math




@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

steps = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']



@pytest.mark.parametrize('link', steps)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    input_1 = browser.find_element_by_css_selector("#ember1597")
    input_1.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_css_selector('#ember1491 > div > div > div.attempt__inner > div.attempt__actions > button')
    button.click()
    time.sleep(1)
    ans_text = browser.find_element_by_css_selector('#ember1670 > pre').text
    assert ans_text == 'Correct!'
