from datetime import date, timedelta  # core python module
import time
import pandas as pd  # pip install pandas

from send_email import send_email  


# Public GoogleSheets url - not secure!
SHEET_ID = "1oxD_I4yzs_X0JbSKi9FtbSE6kZzwYkAjcMoVK-TO0SY" 
SHEET_NAME = "Crypto_Price_alert"  
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if pd.notna(row["reminder_date"]) and (present >= row["reminder_date"].date()):
            send_email(
                subject=f'[Syren0914]',
                receiver_email=row["Email"],
                name=row["Name"],
                Change=row["24H_Change"],
    
                Price=row["Price"],
                
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


while True:
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)

    # Sleep for 24 hours before checking again
    time.sleep(24 * 60 * 60)  # Sleep for 24 hours
