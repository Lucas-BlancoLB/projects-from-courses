import os
import dotenv
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

dotenv.load_dotenv()

price_alert = "1_500.00"
msg = os.getenv("MSG")
amazon_link = os.getenv("AMAZON_link")

h = {"User-Agent": os.getenv("USER_AGENT"),
     "Accept-Language": os.getenv("ACCEPT_LANGUAGE")}

r = requests.get(url=amazon_link, headers=h).text
soup = BeautifulSoup(r, 'lxml')
# print(soup.prettify())

price = soup.select(selector="span .a-offscreen")[0].get_text().split("$")[1].replace('.', '_').replace(',', '.')

if price <= price_alert:
    msg += f"$:{price}."
    try:
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), port=587) as server:
            server.starttls()
            server.login(user=os.getenv("FROM_EMAIL"), password=os.getenv("FM_EMAIL_CODE"))
            server.sendmail(from_addr=os.getenv("FROM_EMAIL"), to_addrs=os.getenv("TO_EMAIL"), msg=msg)
    except Exception as e:
        print(f"An error happened while sending the email: {e}")
