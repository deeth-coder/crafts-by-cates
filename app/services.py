import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Define the scope for the Google Sheets API
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_google_sheet_client():
    """
    Authenticates with Google Sheets using credentials from environment variables
    or a local file.
    """
    creds_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
    
    if creds_json:
        # Load from environment variable (Production/Heroku)
        creds_dict = json.loads(creds_json)
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    elif os.path.exists('credentials.json'):
        # Load from local file (Development)
        creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    else:
        raise ValueError("No Google Sheets credentials found. Set GOOGLE_SHEETS_CREDENTIALS env var or create credentials.json.")

    return gspread.authorize(creds)

def add_email_to_sheet(email):
    """
    Appends an email to the configured Google Sheet.
    """
    sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    if not sheet_id:
        raise ValueError("GOOGLE_SHEET_ID environment variable not set.")

    try:
        client = get_google_sheet_client()
        sheet = client.open_by_key(sheet_id).sheet1
        # Append the email and a timestamp (optional, but good practice)
        # We let the sheet handle the timestamp if we just send the email, 
        # or we can send it here. Let's just send the email for now to keep it simple.
        sheet.append_row([email])
        return True
    except Exception as e:
        print(f"Error adding email to sheet: {e}")
        return False
