import requests
import config
from twilio.rest import Client



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": config.STOCK_API_KEY
}

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
# print(stock_data)
data_list = [value for(key, value) in stock_data.items()]
yesterday_stock = data_list[0]
yesterday_stock_close = yesterday_stock["4. close"]
# print(yesterday_stock_close)

# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_data_close = before_yesterday_data["4. close"]
# print(before_yesterday_data_close)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_stock_close) - float(before_yesterday_data_close))
# print(difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_stock_close)) * 100
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

get_news = False

if diff_percent > 5:
    # print("Get news")
    get_news = True

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
## STEP 2: https://newsapi.org/
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_PARAMETERES = {
        "qInTitle": COMPANY_NAME,
        "apiKey": config.NEWS_API_KEY
    }

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    response1 = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERES)
    response1.raise_for_status()
    news_articles = response1.json()
    news_articles_list = news_articles["articles"][:3]

    print(news_articles_list)


# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.

if get_news:
    for article in news_articles_list:
        client = Client(config.twilio_account_sid, config.twilio_auth_token)
        message = client.messages \
            .create(
            body=f"{article}",
            from_=config.twilio_phone_num,
            to=config.my_phone_num
        )

        print(message.status)




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

