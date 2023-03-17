from email import message
import smtpd
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

host = "smtp.gmail.com"
port = 465

usermane = "elen.bacovska@gmail.com"
password = os.environ.get("PASSWORD_FOR_EMAIL")
message = """\
Subject: Hi
Hi!
Haw are you?
Bye.
"""

receiver = "elen.bacovska@gmail.com"
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(usermane, password)
    server.sendmail(usermane, receiver, message)