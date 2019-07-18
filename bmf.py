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
        cls.driver.maximize_window()  # Maximizing the window size
        cls.driver.implicitly_wait(5) # dding a implicit wait of 5 seconds
        cls.driver.get('https://www.bookmyforex.com/')

    def test_ratealert(self):

        required_exchange_rate = 77.3000 # Setting the Reference Exchange Rate
        required_currency = 'Euro'       # Setting the Reference Exchange Currency
        required_city = 'Bangalore'      # Setting the Reference Exchange Location
        driver = self.driver

        city = driver.find_element_by_xpath('//*[@id="select2-buysell-cityCode-container"]') # Selecting the City
        city.click()
        city_sel = driver.find_element_by_xpath('/html/body/span/span/span[1]/input') # City Text Box
        city_sel.send_keys(required_city) # Location Input
        city_sel.send_keys(Keys.ENTER)  # Location Selection
        sleep(1)
        currency = driver.find_element_by_xpath('//*[@id="buySellForm"]/div[3]/div/div[2]/span/span[1]/span') #Foreign Currency Field
        currency.click()
        currency_sel = driver.find_element_by_xpath('/html/body/span/span/span[1]/input') # Foreign Currency Text box
        currency_sel.send_keys(required_currency)  # Foreign Currency Input
        currency_sel.send_keys(Keys.ENTER)   # Foreign Currency Selection
        sleep(1)
        while True:
            rate_value = driver.find_element_by_xpath('//*[@id="buySellForm"]/div[5]/div/span[1]/span/span').text  # Getting Current Rate
            print(rate_value +"     "+str(datetime.datetime.now()))  # Printing the Update Exchange rate
            if float(rate_value) < required_exchange_rate:
                playsound('test_sound1.mp3')   # If rate drops below specific value
            sleep(16)  # Exchange Refresh Rate




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()