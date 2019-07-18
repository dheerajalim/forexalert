from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
import unittest
from playsound import playsound

class Bmf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.PhantomJS(executable_path='C:\\Development\\phantomjs\\bin\\phantomjs') # or add to your PATH
        cls.driver = webdriver.Chrome(executable_path='C:\\Users\\dheeraja1\\PycharmProjects\\selenium\\chromedriver.exe') # or add to your PATH
        # driver.set_window_size(1024, 768) # optional
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get('https://www.bookmyforex.com/')

    def test_ratealert(self):

        required_exchange_rate = 77.3000
        required_currency = 'Euro'
        driver = self.driver
        currency = driver.find_element_by_xpath('//*[@id="buySellForm"]/div[3]/div/div[2]/span/span[1]/span')
        currency.click()
        currency_sel = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        currency_sel.send_keys(required_currency)
        currency_sel.send_keys(Keys.ENTER)
        sleep(1)
        while True:
            rate_value = driver.find_element_by_xpath('//*[@id="buySellForm"]/div[5]/div/span[1]/span/span').text
            print(rate_value +"     "+str(datetime.datetime.now()))
            if float(rate_value) < required_exchange_rate:
                playsound('test_sound1.mp3')
            sleep(16)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()