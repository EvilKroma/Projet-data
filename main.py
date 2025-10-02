import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

station_id = 8118

url = f"https://api.openaq.org/v3/locations/{station_id}"

headers =   {"X-API-Key": os.getenv("API_KEY")}

# Call API 
response = requests.get(url, headers=headers)
data = response.json()

print(data)