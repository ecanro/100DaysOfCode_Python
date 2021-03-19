from twilio.rest import Client
import config

TWILIO_SID = config.twilio_account_sid
TWILIO_AUTH_TOKEN = config.twilio_auth_token
TWILIO_VIRTUAL_NUMBER = config.twilio_phone_num
TWILIO_VERIFIED_NUMBER = config.my_phone_num


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)