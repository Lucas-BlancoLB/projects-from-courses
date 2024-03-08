import os
import dotenv
# from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, msg):
        dotenv.load_dotenv()

        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        from_number = os.getenv("FROM_NUMBER")  # Str
        to_number = os.getenv("TO_NUMBER")  # Str
        client = Client(account_sid, auth_token)
        message = client.message \
                        .create(
            body=msg,
            from_=from_number,
            to=to_number,
        )
        print(message.sid)
