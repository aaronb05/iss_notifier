import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(body):
    my_email = os.getenv("my_email")
    password = os.getenv("password")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="aboyles05@gmail.com",
            msg=f"Subject: Look Up! The ISS is above you\n\n  {body}")


