import os
from dotenv import load_dotenv
import datetime as dt
import smtplib


# There are 101 quotes

def format_text(text):
    current_line = ""
    formatted = []
    max_character = 75
    words = text.strip().split()

    for word in words:

        if (len(current_line) + len(word)) <= max_character:
            current_line += word + " "
        else:
            formatted.append((current_line + "\n"))
            current_line = word + " "

    if current_line:
        formatted.append(current_line.strip())

    formatted_text = "".join(formatted)
    var = formatted_text.replace(" - ", "\n- ")
    var = var.replace("- \n", "- ")
    return var


with open("quotes.txt") as file:
    data = file.readlines()
try:
    with open("num_quotes_save.txt") as save:
        num_save = save.read()
except FileNotFoundError:
    with open("num_quotes_save.txt", mode="w") as file:
        file.write("0")
        num_save = "0"
finally:
    num_save = int(num_save)
    print(type(num_save))


now = dt.datetime.now()

if now.weekday() == 0 and now.hour == 12:
    load_dotenv()
    credentials = [os.getenv("SMTP_MAIL"), os.getenv("from_email"), os.getenv("password"), os.getenv("to_email")]
    
    with smtplib.SMTP(credentials[0], port=587) as server:
        server.starttls()  # For security proposes — encryption protocol
        server.login(user=credentials[1], password=credentials[2])
        server.sendmail(from_addr=credentials[1],
                        to_addrs=credentials[3],
                        msg=f"Subject: Don't forget you're awesome!!\n\n{format_text(data[num_save])}")
        if num_save >= 101:
            num_save = 0
        else:
            num_save += 1
        with open("num_quotes_save.txt", mode="w") as file:
            file.write(str(num_save))
