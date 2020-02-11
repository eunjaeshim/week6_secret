import requests
import secret

base_url = 'https://newsapi.org/v2/top-headlines'
NEWSAPI_KEY = secret.NEWSAPI_KEY
params = {
    "q":"new hampshire",
    "apiKey": NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
articles = result["articles"]

for i in range(len(articles)) :
    if "new hampshire" in articles[i]["title"].lower() :
        print(f"{articles[i]['title']}")
