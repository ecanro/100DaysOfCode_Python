from selenium import webdriver

chrome_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.amazon.es/s?k=amd+ryzen+7+5800x&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

# Find element
price = driver.find_element_by_class_name("a-price-whole")
print(price.text)
search_bar = driver.find_element_by_name("field-keywords")
print(search_bar.get_attribute("aria-label"))
logo = driver.find_element_by_id("nav-logo-sprites")
print(logo.size)
image_link = driver.find_element_by_css_selector(".a-section img")
print(image_link.size)

# Find element(s)
prices = driver.find_elements_by_class_name("a-price-whole")
for _ in prices:
    print(_.text)

# if we have difficult to find a element use XPath
# maybe a submit link?
driver.get("https://www.python.org/")
bug_link = driver.find_element_by_xpath("//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(bug_link.text)




#driver.close()
#driver.quit()