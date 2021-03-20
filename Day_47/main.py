import requests
import smtplib
from bs4 import BeautifulSoup
import config
import lxml

url = "https://www.amazon.com/s?k=amd+ryzen+7+5800x&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "es,pt;q=0.9,es-ES;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(name="span", class_="a-size-medium a-color-base a-text-normal").get_text().strip()
print(title)

BUY_PRICE = 300

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(config.email, config.password)
        connection.sendmail(
            from_addr= config.email,
            to_addrs= config.email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )