import smtplib
import config


class NotificationManager:

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(config.email, config.password)
            for email in emails:
                connection.sendmail(
                    from_addr=config.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

