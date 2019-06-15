from selenium import webdriver
import time

import unittest


def test_page(link):
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("input[class='form-control first']:required")
    input1.send_keys("ololo")
    input2 = browser.find_element_by_css_selector("input[class='form-control second']:required")
    input2.send_keys("ololo")
    input3 = browser.find_element_by_css_selector("input[class='form-control third']:required")
    input3.send_keys("ololo")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    return welcome_text


class TestAbs(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(test_page('http://suninjuly.github.io/registration1.html'), "Поздравляем! Вы успешно зарегистировались!", "Не правильный ответ")

    def test_link2(self):
        self.assertEqual(test_page('http://suninjuly.github.io/registration2.html'), "Поздравляем! Вы успешно зарегистировались!", "Не правильный ответ")


if __name__ == "__main__":
    unittest.main()