import os
import dotenv
import requests
import datetime as dt
import twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL_alphavantage = "https://www.alphavantage.co/query"
URL_newsapi = "https://newsapi.org/v2/everything"

TWILIO_SID = None  # TO_DEFINE
TWILIO_AUTH_TOKEN = None  # TO_DEFINE
dotenv.load_dotenv()


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("API_KEY"),
}
news_params = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "q": COMPANY_NAME,
    "pageSize": 3
}


def difference_percentage(old_num:float, new_num:float):
    difference = old_num - new_num
    return round((difference / old_num) * 100, 2)


def format_txt(text:str) ->str:
    index_txt = text.find("…")
    if index_txt != -1:
        return  text[:index_txt + 1]
    else:
        return text


r = requests.get(URL_alphavantage, params=parameters)
r.raise_for_status()
data = r.json()['Time Series (Daily)']


today = dt.datetime.now()
yesterday = str(today - dt.timedelta(days=1)).split()[0]


percentage = difference_percentage(float(data[yesterday]['1. open']), float(data[yesterday]['4. close']))

result = None
if percentage > 5 or percentage < -5:
    if percentage > 0:
        result = f"{STOCK} 🔺{percentage}"
    if percentage < 0:
        result = f"{STOCK} 🔻{percentage}"


r_2 = requests.get(URL_newsapi, params=news_params)
r_2.raise_for_status()
three_articles = r_2.json()['articles']


if result is not None:
    msg = [f"{result}\nHeadline: {x['title']}\nBrief: {format_txt(x['content'])}" for x in three_articles]
    for article in msg:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_="TWOLIO_VIRTUAL_NUMBER",  # TO_DEFINE
            to="PERSONAL_NUMBER"  # TO_DEFINE
        )
