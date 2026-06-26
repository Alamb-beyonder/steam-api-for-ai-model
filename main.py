from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("STEAM_API_KEY")
url = f"https://api.steampowered.com/IStoreService/GetAppList/v1/?key={api_key}"

response = requests.get(url)

print(response.status_code)
data = response.json()
print(data["response"]["apps"])

