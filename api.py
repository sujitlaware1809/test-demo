import requests
import os
from werkzeug.utils import secure_filename

# Strava App Credentials
CLIENT_ID = '<your client id>'
CLIENT_SECRET = '<your client secret>'
REDIRECT_URI = 'http://localhost:5000/exchange_token'
GOOGLE_API_KEY = '<your api key>'

def generate_auth_url():
    auth_url = (
        f"https://www.strava.com/oauth/authorize"
        f"?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
        f"&response_type=code&scope=read,activity:read_all"
    )
    return auth_url

def exchange_token(code):
    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()  # Contains access_token
    
    else:
        print("Error exchanging token:", response.status_code, response.text)
        return None
    
def get_user_data(access_token):
    url = "https://www.strava.com/api/v3/athlete"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print("Error retrieving user data:", response.status_code, response.text)
        return None
