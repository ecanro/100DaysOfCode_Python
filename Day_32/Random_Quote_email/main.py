import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = "Your Email"
MY_PASSWORD = "Yoru Password"
PLACEHOLDER = "[name]"

data = pandas.read_csv("../Automated_Birthday_Wisher/birthdays.csv")
all_birthdays = data.month.to_list()
print(all_birthdays)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote_of_day = random.choice(all_quotes)
    print(quote_of_day)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="MAIL",
            msg=f"Subject:Quote of Motivation\n\n{quote_of_day}"
        )




# print(day_of_week)

# data_of_birth = dt.datetime(year=1977, month=4, day=25, hour=13)
# print(data_of_birth)
