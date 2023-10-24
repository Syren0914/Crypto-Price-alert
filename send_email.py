import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def extract_percentage_change(Change):
    # Use a regular expression to extract the numeric part (including a possible decimal point) from Change
    match = re.search(r"[-+]?\d*\.\d+|\d+", Change)
    if match:
        return float(match.group())
    return 0.0  # Default value if no match is found

def send_email(subject, receiver_email, name, Price, Change):
    # Create the base text message.
    msg = MIMEMultipart()
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Syren0914", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    percentage_change = extract_percentage_change(Change)

    # HTML content with improved aesthetics
    msg.set_content(
            f"""\
        Dear Mr.Erdene for todays value <strong> {name} </strong> price is {Price} USD,
   
        Thank you for using our service. :D
        Best regards
        Syren0914
        """
        )
    msg.add_alternative(
        f"""\
        <html>
     <body>
        Dear Mr. Erdene,
        <br><br>
        We're excited to bring you the latest update! <strong>{name}</strong> is currently valued at <span style="color: green">{Price} USD</span>. 🚀
        <br><br>
        But the real fun begins when you check the change - it's dancing around with <span style="color: {'green' if percentage_change > 0 else 'red'}">{Change}</span> in value! 🎉
        <br><br>
        Thank you for being part of our journey, and we promise to keep the good vibes coming your way.
        <br><br>
        Wishing you a day filled with excitement and joy,
        <br>
        Syren0914 🌟
         </body>
        </html>

        """,
        subtype = "html",
        

    )
    


    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email(
        subject="Crypto Price Alert",
        name="BTC",
        receiver_email="msrgaming35@gmail.com",
        Change="-15.13% (1d)",
        Price="33,000 USD",
        
    )
