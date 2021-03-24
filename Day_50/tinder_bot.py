# we will create a tinder bot for "dislike for 100 wipes a day"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import config

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.window_handles
driver.get("https://tinder.com/")

# ok we begins to find the login button
time.sleep(3)
register_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
register_button.click()

# after find the fb login button
time.sleep(3)
start_with_fb_button = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
start_with_fb_button.click()

# now some new thing: we need to change for the popup windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# and now can fill the inputs form
time.sleep(3)
fb_login = driver.find_element_by_xpath('//*[@id="email"]')
fb_login.send_keys(config.email)
fb_passw = driver.find_element_by_xpath('//*[@id="pass"]')
fb_passw.send_keys(config.passw, Keys.ENTER)

# switch for the main page
driver.switch_to.window(base_window)

#Delay by 5 seconds to allow page to load.
time.sleep(3)

# Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()