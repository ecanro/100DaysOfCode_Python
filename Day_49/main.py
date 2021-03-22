# automatic job application in linkedin ._.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
# the link is for porto-portugal and activate the easy apply button
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# login
login_button = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
login_button.click()

# Wait for the next page to load.
time.sleep(3)

# fill fields
email = driver.find_element_by_id("username")
email.send_keys(config.email, Keys.ENTER)
password = driver.find_element_by_id("password")
password.send_keys(config.passw, Keys.ENTER)

# now get the job list
jobs_list = driver.find_elements_by_class_name("job-card-list__title")
for job in jobs_list:
    # get the links
    print(job.get_attribute("href"))
    # get the titles
    print(job.text)

# now apply to the firts jobs, we need to find the apply button
apply_button = driver.find_element_by_class_name('jobs-apply-button')
apply_button.click()

# now I have fill all fields, so only need the clic to apply
send_apply = driver.find_element_by_xpath('//*[@id="ember393"]/span')
send_apply.click()

# close the modal windows
time.sleep(2)
close = driver.find_element_by_xpath('//*[@id="ember414"]')
close.click()

