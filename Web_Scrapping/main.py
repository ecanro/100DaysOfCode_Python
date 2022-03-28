#
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import requests
# import config
#
# URL_LDS = "https://www.churchofjesuschrist.org/?lang=eng"
#
# chrome_driver_path = "C:\WebDriver\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# web = driver.get(URL_LDS)
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
#
# # response = requests.get(url=URL_LDS, headers=header)
# # soup = BeautifulSoup(response.text, "html.parser")
# # print(soup.prettify())
#
# # Accept cookies
# cookies_button = driver.find_element_by_id('truste-consent-button')
# cookies_button.click()
#
# # Get profile button on click
# #driver.switch_to.frame(driver.find_element_by_tag_name('pf-navbar'))
# profile_button = driver.find_element_by_class_name('profileButton')
# profile_button.click()
# for e in driver.find_elements_by_tag_name('span'):
#     if e.get_property('id') == 'profile':
#         print(e)
#         e.click()
#         break

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://lds.org")
#     print(page.title())
#     browser.close()

# import asyncio
# from playwright.async_api import async_playwright
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("http://lds.org")
#         print(await page.title())
#         await browser.close()
#
# asyncio.run(main())

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("http://lds.org/")
    page.screenshot(path="example.png")
    browser.close()

