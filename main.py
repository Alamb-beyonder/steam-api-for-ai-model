from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
api_key = os.getenv("STEAM_API_KEY")

apps = []
last_appid = None

url = "https://api.steampowered.com/IStoreService/GetAppList/v1/"
params = {"key": api_key, "include_games": 1}
pages = 0

while True:
    
    # Add last_appid parameter to params. An existing last_appid means existing batch
    if last_appid:
        params["last_appid"] = last_appid

    response = requests.get(url, params=params)
    data = response.json()
    apps.extend(data["response"]["apps"])
    pages += 1

    print(f"Fetched {pages} pages - {len(apps)} apps")

    # If have_more_apps is false, appending is done 
    if not data["response"].get("have_more_results", False):
        break
    
    #If have_more_apps is true, continue onto next batch. Use get() for error handling
    last_appid = data["response"]["last_appid"]

with open("steams_apps.json", "w") as file:
        json.dump(apps, file)

print("Complete!")

