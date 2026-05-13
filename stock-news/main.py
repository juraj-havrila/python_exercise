import requests
import datetime as dt
import pandas
import time
import smtplib

my_email = "x"
my_password = "x"

data = pandas.read_csv("stocks.csv")
my_stocks={row['ticker']:(row['trigger_value'],row['trigger_delta']) for (index,row) in data.iterrows()}


#now = dt.datetime.now()
#date_yesterday = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
today = dt.date.today()
yesterday = str(today - dt.timedelta(days = 1))
day_before_yesterday = str(today - dt.timedelta(days = 2))
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_AV = "x"
API_KEY_NA = "x"

my_email_content=''





def check_prices(stock,trigger_value,trigger_delta):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": API_KEY_AV,
    }
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()

    print (response.json())

    stock_data = response.json()['Time Series (Daily)']

    price_open_before_yesterday = float(stock_data[day_before_yesterday]['1. open'])
    price_close_yesterday = float(stock_data[yesterday]['4. close'])

    price_high_before_yesterday = float(stock_data[day_before_yesterday]['2. high'])
    price_low_before_yesterday = float(stock_data[day_before_yesterday]['3. low'])
    price_high_yesterday = float(stock_data[yesterday]['2. high'])
    price_low_yesterday = float(stock_data[yesterday]['3. low'])

    if get_change(price_open_before_yesterday, price_close_yesterday) > trigger_delta:
        trigger_percentage = True
    else:
        trigger_percentage =  False

    #if min(price_open_before_yesterday, price_close_yesterday) <= trigger_value <=max(price_open_before_yesterday, price_close_yesterday):
    if min(price_low_before_yesterday, price_low_yesterday) <= trigger_value <= max(price_high_yesterday, price_high_before_yesterday):
        trigger_price = True
    else:
        trigger_price =  False

    if trigger_percentage or trigger_price:
        return True
    else:
        return False



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
        "language": "en",
        "apiKey": API_KEY_NA,

    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()

    return response.json()['articles'][0:2]


def send_mail(email_content):
     #print(email_content)
     with smtplib.SMTP('smtp.gmail.com', 587) as connection:
         connection.starttls()
         connection.login(my_email, my_password)
         connection.sendmail(
             from_addr=my_email,
             to_addrs="x",
             msg=f"Subject:Stock News\n\n{email_content}"
         )


#####################################################################################################

for my_ticker in my_stocks.keys():
    time.sleep(21) #free tier in the api only allows 5 calls per minute
    #my_email_content = ''
    #print(my_stocks[my_ticker][1])
    t_value = float(my_stocks[my_ticker][0])
    t_percent =float(my_stocks[my_ticker][1])
    if check_prices(my_ticker,t_value,t_percent):
        my_news=get_news(my_ticker)
        my_email_content += f"{my_ticker} \n -------------------------------------------- \n"
        for my_article in my_news:
            my_email_content += f"{my_article['title']} \n {my_article['description']} \n\n{my_article['url']} \n ______________\n\n"

if (my_email_content):
    send_mail(my_email_content)


#####################################################################################################





#if check_prices(STOCK):
#    my_news = get_news(STOCK)
#    print(my_news)

#my_news = get_news(STOCK)
#print(my_news)





#print(stock_data)

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
"You don't rise to the level of your goals, you fall to the level of your systems " is a quote that comes to mind.
"""

