# Crypto Price Alert

Crypto Price Alert is a Python script that periodically checks a Google Sheets document for reminders related to cryptocurrency prices and sends email alerts for those reminders.

## Features

- **Reminder System**: Uses a Google Sheets document to store reminders about cryptocurrency prices.
- **Email Notifications**: Sends email notifications to users when their reminders are due.
- **Periodic Checking**: Continuously checks for reminders and sends emails accordingly.

## Requirements

- Python 3.x
- pandas library (`pip install pandas`)
- `send_email.py` module for sending emails (not provided, must be implemented separately)
- Google Sheets API access (via SHEET_ID and SHEET_NAME)
- Google account with access to the Google Sheets document

## Setup

1. Clone the repository or download the script.
   
2. Install the required libraries: pip install pandas

3. Implement the `send_email.py` module for sending emails. This module should contain a function `send_email` that takes necessary arguments like `subject`, `receiver_email`, `name`, `Change`, `Price`, etc. This function should handle sending emails.

4. Set up a Google Sheets document with the necessary reminder data. Make sure to note the SHEET_ID and SHEET_NAME.

5. Replace the `SHEET_ID` and `SHEET_NAME` constants in the script with your Google Sheets document's ID and sheet name.

6. Run the script: python crypto_price_alert.py

   
7. The script will start checking for reminders and sending emails accordingly.

## Usage

- Add reminders to the Google Sheets document in the format specified.
- Run the script and keep it running to continuously monitor for reminders and send email alerts.

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or feature implementations, feel free to open an issue or create a pull request.

## License

[MIT License](LICENSE)




