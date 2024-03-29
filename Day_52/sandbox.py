from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import config

CHROME_DRIVER_PATH = "C:\WebDriver\chromedriver.exe"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = config.email
PASSWORD = config.passw


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # detect any other button
        consent_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        consent_button.click()

        # start session with  FB credentials
        fb_button = self.driver.find_element_by_class_name('KPnG0')
        fb_button.click()

        # detect any other button
        consent_button = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]')
        consent_button.click()

        username = self.driver.find_element_by_id("email")
        password = self.driver.find_element_by_id("pass")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(1)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(8)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
