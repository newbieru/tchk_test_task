import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TochkaAuthorizationForm(unittest.TestCase):
    def setUp(self):
        url = 'https://enter.tochka.com/sandbox/v1/login/'
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_1_1(self):
        chrome = self.driver
        wait = WebDriverWait(chrome, 5)

        login_box = chrome.find_element(By.ID, 'username')
        login_box.send_keys('sandbox')
        pswd_box = chrome.find_element(By.ID, 'password')
        pswd_box.send_keys('sandbox')
        chrome.find_element(By.CSS_SELECTOR, "button.tochka-button").click()            # click "submit button"
        phone_code = wait.until(EC.element_to_be_clickable((By.ID, 'code_input')))
        phone_code.send_keys('12345')

        chrome.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()               # chose 1st of available rights
        chrome.find_element(By.CSS_SELECTOR, "button.access-list__button").click()      # click "submit" button

        assert 'code' in chrome.current_url                                             # check the 'code' in url

    def test_1_2(self):
        chrome = self.driver

        login_box = chrome.find_element_by_id('username')
        login_box.send_keys('sandbox')
        pswd_box = chrome.find_element_by_id('password')
        pswd_box.send_keys('sadbox')
        chrome.find_element_by_css_selector("button[type = 'submit']").click()          # click "submit" button

        assert 'login__error' in chrome.page_source                                     # check error occured

    def test_1_3(self):
        chrome = self.driver

        login_box = chrome.find_element_by_id('username')
        login_box.send_keys('sadbox')
        pswd_box = chrome.find_element_by_id('password')
        pswd_box.send_keys('sandbox')
        chrome.find_element_by_css_selector("button[type = 'submit']").click()          # click "submit" button

        assert 'login__error' in chrome.page_source                                     # check error occured

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





