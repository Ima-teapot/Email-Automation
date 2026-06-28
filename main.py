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

def email(rate):

    email = "sender@gmail.com"
    app_pass = "email pass"

    receiver_email = ["receiver@gmail.com"]

    date = datetime.date.today()
    for i in receiver_email:
        msg = EmailMessage()
        msg["Subject"] = "Rate of Different Currencies"
        msg["From"] = f"Someone<{email}>"
        msg["To"] = i
        msg.set_content(f"""
        Dear Customer,
        I hope you are doing well.
        Please find Different Currency Rate:
        Date: {date}
        Currency Rate:
        {rate}
        Thank you for your continued support.
        Best Regards,
        name   
                                            
                            """)
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email,app_pass)
        server.send_message(msg)
        print("Email sent")