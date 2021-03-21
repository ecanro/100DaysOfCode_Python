from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# add the chrome driver
chrome_driver ="C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
# some web sites styles adjust the elements in the size screen and we maybe see less elements
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# we need get the the article statistic, we can use xpath
statistics = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(statistics.text)
# or use any other methods
statistics = driver.find_element_by_css_selector("#articlecount a")
print(statistics.text)

# and now we wants to click in this element
#statistics.click()

# we can find any element by link text
wiki_portals = driver.find_element_by_link_text("All portals")
#wiki_portals.click()

# or search some in a search input
search = driver.find_element_by_name("search")
search.send_keys("Python", Keys.ENTER)