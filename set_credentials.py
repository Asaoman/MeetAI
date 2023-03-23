import os
import json

# Replace 'path/to/your/json_file.json' with the actual path to your JSON file
with open('E:\zFilms Dropbox\z Films\VS_Code\MeetAI\client_secret_824775997781-nvvr0fdv8lhs565kl2rmfldkjfcv5305.apps.googleusercontent.com.json', 'r') as file:
    credentials_json = json.load(file)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json.dumps(credentials_json)
