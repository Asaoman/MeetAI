import set_credentials

import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load the credentials from the environment variable
credentials_json = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
credentials = service_account.Credentials.from_service_account_info(
    credentials_json,
    scopes=['https://www.googleapis.com/auth/calendar']
)

# Create a Google Calendar API client
calendar_api = build('calendar', 'v3', credentials=credentials)

# Your code that uses the Google Calendar API
