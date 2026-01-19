from dotenv import load_dotenv
from os import getenv
from smtplib import SMTP_SSL
from email.message import EmailMessage

from argparse import ArgumentParser
parser = ArgumentParser(description="CLI email sender")

load_dotenv()

parser.add_argument("--to", required= True, help="Reciver Email")
parser.add_argument("--sb", required= True, help="Email Subject")
parser.add_argument("--msg", required= True, help="Email Message")
# parser.add_argument("--to", required= True, help="Reciver Email")
#

args = parser.parse_args()

msg = EmailMessage()

APP_PASSWORD = getenv("EMAIL_API")
MY_EMAIL = "rakeshkund3355@gmail.com"

msg["From"] = MY_EMAIL
msg["To"] = args.to
msg["Subject"] = args.sb
msg.set_content(args.msg)



try:
    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(MY_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print("sent")
except Exception:
    print(Exception)
