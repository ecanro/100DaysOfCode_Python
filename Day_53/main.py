from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
import requests
import time
import config

# TODO: we need to create a little app for search in the ZILLOW web some information
# TODO: after we recollect the information and so send via google form to a google spread cheat

# TODO: first start to get the data with Beautiful Soup to scrapping the web
URL_ZILLOW = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.52465285253906%2C%22east%22%3A-122.34200514746094%2C%22south%22%3A37.66911009166429%2C%22north%22%3A37.88132053431091%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# the header is very important because the web can detect is not a human to navigate
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=URL_ZILLOW, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

all_link_buildings = soup.select(".list-card-top a")[:1]
# print(all_buildings)
# building_link = [building.getText() for building in all_buildings]

# Get the links
all_links = []

for link in all_link_buildings:
    href = link["href"]

    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
    # print(href)

# print(all_links)

# Get the addresses
all_address_buildings = soup.select(".list-card-info address")
# print(all_address_buildings)
all_addresses = [address.getText().split(" | ")[-1] for address in all_address_buildings]
# print(all_addresses)

# Get the prices
# all_prices_buildings = soup.select(".list-card-details li")->works but prices have different structures
all_price_buildings = soup.select(".list-card-heading")
all_prices = []
# print(all_prices_buildings)
# comprehension list work fine but need another structure to get all the prices
# all_prices = [price.getText().split("+")[0] for price in all_prices_buildings if "$" in price.text]
for n in all_price_buildings:
    try:
        # only one price listing
        price = n.select(".list-card-price")[0].contents[0]
    except IndexError:
        # multiple listing prices
        print("Multiple listing for the card")
        price = n.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
# print(all_prices)

# TODO: Using Selenium, now with this information we need fill the google form
# using selenium
GOOGLE_FORM_LINK = config.google_form
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_LINK)

    # waiting
    time.sleep(2)

    # get the html elements in the form
    address = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')

    # fill the input fields in the form
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit.click()

driver.close()

# TODO: create the Spreadsheet
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(config.request_form_link)
spreadsheet_button = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span')
spreadsheet_button.click()