import requests

response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
print(response.status_code)
data = response.json()

