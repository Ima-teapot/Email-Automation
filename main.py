import datetime
import requests
import smtplib
from email.message import EmailMessage
import schedule
import time
def Currency_rate():
    api_keys = "cur_live_6R6UWfRoJROKxxp5tj0Z6vHpYIn714yggSbaB7Wz"
    link = f"https://api.currencyapi.com/v3/latest?apikey={api_keys}&basecurrency=USD&currencies=BDT,INR,EUR"
    r = requests.get(link)
    data = r.json()

    return f"*Bangladesh currency rate:{data["data"]["BDT"]["value"]} dollar \n * INR:{data["data"]["INR"]["value"]} dollar \n *EUR:{data["data"]["EUR"]["value"]} dollar"

