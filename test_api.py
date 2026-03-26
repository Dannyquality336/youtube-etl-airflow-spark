import requests

key = "AIzaSyD-ZiqFGqlNYCICFmoPtTQUxT6UtHLw6NU"

url = "https://www.googleapis.com/youtube/v3/playlists"

params = {
    "part": "snippet",
    "id": "PLrAXtmRdnEQy6nuLMHjMZOz59W60d6H1V",
    "key": key,
}

r = requests.get(url, params=params)

print(r.json())