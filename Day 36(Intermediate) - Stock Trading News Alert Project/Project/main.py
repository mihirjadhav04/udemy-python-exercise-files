import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = "6RX4M2PHY9124WBP"
NEWS_API_KEY = "77cff91bc92f4d2cac3478d7e28f35af"
TWILIO_ACCOUNT_SID = "AC209f6a3929bbad64d6793634567c9aa5"
TWILIO_AUTH_TOKEN = "462bfde51c56002d984c83fb52a5c655"

parameters = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}
# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params=parameters)
# print(response.status_code)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
# print(yesterday_data)
yesterday_close_price = yesterday_data["4. close"]
# print(yesterday_close_price)

# Get the day before yesterday's closing stock price
day_before_yesterday = data_list[1]
day_before_yesterday_close_price = day_before_yesterday["4. close"]
# print(day_before_yesterday_close_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_close_price) - float(day_before_yesterday_close_price))
# print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_close_price)) * 100
# print(diff_percent)

# If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 2:
    print("Great News!!")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    parameters = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT, params=parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    # print(articles)

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    # print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"Headline: {article['title']}, Breif:{article['description']}"
        for article in three_articles
    ]
    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18503603556",
            to="+919137739416",
        )

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
