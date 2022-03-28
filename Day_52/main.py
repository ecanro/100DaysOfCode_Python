from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import config

CHROME_DRIVER_PATH = "C:\WebDriver\chromedriver.exe"
INSTAGRAM_EMAIL = config.email
INSTAGRAM_PASSWORD = config.passw


class instagramFollows:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def instagram_follows(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        # detect any other button
        consent_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        consent_button.click()


bot = instagramFollows(CHROME_DRIVER_PATH)
bot.instagram_follows()