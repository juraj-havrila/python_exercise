import requests
import datetime as dt

#now = dt.datetime.now()
#date_yesterday = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
today = dt.date.today()
yesterday = str(today - dt.timedelta(days = 1))
day_before_yesterday = today - dt.timedelta(days = 2)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_AV = "x"
API_KEY_NA = "x"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_AV,
}
def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 101

def get_news(stock):
    parameters = {
        "q": stock,
        "from": yesterday,
        "sortBy":"popularity",
        "apiKey": API_KEY_NA,

    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()

    return response.json()[0:2]






response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]

price_close_yesterday= int(stock_data[day_before_yesterday]['1. open'])
price_close_yesterday= int(stock_data[yesterday]['4. close'])

if get_change(price_close_yesterday, price_close_yesterday) > 5:

    my_news = get_news(STOCK)





print(stock_data)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

