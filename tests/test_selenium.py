import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AuthYandex(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url='https://passport.yandex.ru/auth/')
        self.login = 'your_YANDEX_LOGIN'
        self.password = 'your_PASSWORD'

    def test_auth(self):
        login = self.driver.find_element(By.NAME, 'login')
        login.send_keys(f'{self.login}', Keys.ENTER)
        time.sleep(4)
        password = self.driver.find_element(By.NAME, 'passwd')
        password.send_keys(f'{self.password}', Keys.ENTER)
        time.sleep(5)
        assert self.driver.current_url.split('/')[-1] == 'profile'

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
