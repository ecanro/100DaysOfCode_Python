from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import config

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.maximize_window()
driver.window_handles
driver.get("https://www.speedtest.net/")

time.sleep(2)
# detect any other button
consent_button = driver.find_element_by_class_name("evidon-barrier-acceptbutton")
consent_button.click()

# detect go button
go_button = driver.find_element_by_class_name("start-text")
# base_window = driver.window_handles[0]
go_button.click()

# my promise speed internet
PROMISED_DOWN = 400
PROMISED_UP = 200

# detect any other button
time.sleep(40)
driver.find_element_by_xpath("//html").click();

# close_button = driver.find_element_by_class_name("close-btn")
# close_button.click()

# get data
speed_down = driver.find_element_by_class_name("download-speed").text
print(speed_down)

speed_up = driver.find_element_by_class_name("upload-speed").text
print(speed_up)

# twitter
TWITTER_EMAIL = config.email
TWITTER_PASSW = config.passw


