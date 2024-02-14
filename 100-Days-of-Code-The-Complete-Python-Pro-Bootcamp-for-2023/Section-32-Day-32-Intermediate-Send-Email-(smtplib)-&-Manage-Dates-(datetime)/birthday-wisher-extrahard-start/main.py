import os
import random
from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import smtplib


# load_information
load_dotenv()
credentials = [os.getenv("person_1").splitlines(), os.getenv("person_2").splitlines(), os.getenv("person_3").splitlines()]

# Open letters
with open("letter_templates/letter_1.txt") as x, open("letter_templates/letter_2.txt") as y, open("letter_templates/letter_3.txt") as z:
    letters = [x.read(), y.read(), z.read()]


# Read birthday.csv
df = pd.read_csv("birthdays.csv",index_col=0)


# re-write and create new rows if needed
for i in range(0, len(credentials)):
    credence = credentials[i]
    df.loc[i] = {"namew":credence[0], "email":credence[1], "year":int(credence[3]), "month":int(credence[4]), "day":int(credence[5])}

# save df if
df.to_csv("birthdays.csv")

# current time mm/dd/yy...
time = dt.datetime.now()

# check if it's b-day time within the credentials
for  credence  in credentials:
    month, day = int(credence[4]), int(credence[5])
    if time.month  == month and time.day == day:

        # if it's then send an email
        letter = random.choice(letters).replace("[NAME]", credence[0])
        with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as server:
            server.starttls()
            server.login(user=credentials[0][1], password=credentials[0][2])
            server.sendmail(from_addr=credentials[0][1], to_addrs=credence[1], msg=f"Subject: Happy birthday\n\n{letter}")
            print("send")


##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.