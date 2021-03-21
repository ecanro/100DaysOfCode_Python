from selenium import webdriver

chrome_driver ="C:\Development\chromedriver.exe"
# some web sites styles adjust the elements in the size screen and we maybe see less elements
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.maximize_window()
driver.get("https://www.python.org/")

# we need find all upcoming events
events = {}

# using css selector and work fine
events_dates = driver.find_elements_by_css_selector(".event-widget li time")
for date in events_dates:
    print(date.text)

#using class name and work fine
events_names = driver.find_elements_by_class_name("event-widget li a")
for event in events_names:
    print(event.text)

# now we have every date require in separated code
# we need put together
for n in range(len(events_dates)):
    events[n] = {
        "date": events_dates[n].text,
        "name": events_names[n].text
    }

print(events)