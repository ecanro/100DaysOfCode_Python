from selenium import webdriver

# add the chrome driver
chrome_driver ="C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
# some web sites styles adjust the elements in the size screen and we maybe see less elements
# driver.maximize_window()
driver.get("http://secure-retreat-92358.herokuapp.com/")

# we need to fill the form with selenium
form_fname = driver.find_element_by_name("fName")
form_fname.send_keys("Edgar")
form_lname = driver.find_element_by_name("lName")
form_lname.send_keys("Canro")
form_email = driver.find_element_by_name("email")
form_email.send_keys("edgar.canro@gmail.com")

# now we need to click in the button "Sing Up"
form_submit = driver.find_element_by_tag_name("button")
form_submit.click()
# this will work very nice!!!

driver.get("https://www.appbrewery.co/p/newsletter")
subscribe_input = driver.find_element_by_name("email")
subscribe_input.send_keys("edgar.canro@gmail.com")
subscribe_button = driver.find_element_by_name("commit")
subscribe_button.click()
# and work fine!!!
