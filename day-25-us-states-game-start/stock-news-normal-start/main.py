from requests_cache import CachedSession
import requests
import smtplib
import ssl
import socket
from email.message import EmailMessage

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "2174JI1QXK3RV4UQ"
news_api_key = "301293621584477fa150adbce4fa6fa6"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_email = "wenxin.zhou@warriorlife.net"
password = "hwuyzfpltveykgzq"

stock_parameters = {
    "apikey": stock_api_key,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
}

session = CachedSession("stock_api_cache", expire_after=3600)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = session.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()

last_close = next(iter(stock_data['Time Series (Daily)'].items()))
closing_price = last_close[1]["4. close"]
# print(type(closing_price))
closing_price = round(float(closing_price), 2)

#TODO 2. - Get the day before yesterday's closing stock price

stock_data_list = [value for key, value in stock_data.items()]
old_closing_price = float(list(stock_data_list[1].values())[1]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

abs(1 - 2)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percent_difference = ((closing_price - old_closing_price) / old_closing_price) * 100
print("percent_difference:", percent_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# if percent_difference > 5:
#     print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#if percent_difference > 5:
response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
response.raise_for_status()
articles = response.json()

related_articles = (articles["articles"])

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

articles_list = related_articles[0:3]
print(articles_list)

#print(articles[0:1:2])

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 articles' headline and description using list comprehension.

articles_summary = [x["title"] + "+" + x["description"] for x in articles_list]
print(articles_summary)

#TODO 9. - Send each article as a separate message via Twilio.
ctx = ssl.create_default_context()
percentage = round(percent_difference)

if percentage >= 0:
    icon = "🔺"
else:
    icon = "🔻"

# if abs(percent_difference) > 0:

for x in articles_summary:
    parts = x.split("+")

    # msg = EmailMessage()
    # msg["Subject"] = f"TSLA: {icon}{percentage}%"
    # msg["From"] = my_email
    # msg["To"] = "jenniferzhou3413@gmail.com"
    # msg.set_content(f"Headline: {x[1]} (TSLA)?.\n Brief: {x[2]}")
    #
    # ctx = ssl.create_default_context()
    # try:
    #     print("Attempting to send email...")
    #
    #     raw_socket = socket.create_connection(("smtp.gmail.com", 587), timeout=30)
    #
    #     with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as s:
    #         s.sock = raw_socket
    #
    #         s.set_debuglevel(1)
    #
    #         s.ehlo()
    #         s.starttls(context=ctx)
    #         s.ehlo()
    #
    #         print("Logging in...")
    #         s.login(my_email, password)
    #
    #         print("Sending message...")
    #         s.send_message(msg)
    #         print("Email sent successfully!")
    #
    # except Exception as e:
    #     print(f"\nCaught an error: {e}")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls(context=ctx)
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jenniferzhou3413@gmail.com",
            msg=f"Subject:TSLA: {icon}{percentage}%\n\nHeadline: {parts[0]} (TSLA)?.\n Brief: {parts[1]}",
        )

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
