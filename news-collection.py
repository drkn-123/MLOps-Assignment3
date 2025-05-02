import requests, csv
from datetime import datetime

API_KEY = "953eea93e4234be08e5012163066de26"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
FILENAME = "news_data.csv"

res = requests.get(URL)
data = res.json()

if res.status_code != 200 or data.get("status") != "ok":
    print("API Error:", data)
else:
    articles = data["articles"]
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RunTime", "Title", "Source", "PublishedAt", "URL"])
        for article in articles:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                article["title"],
                article["source"]["name"],
                article["publishedAt"],
                article["url"]
            ])
    print("News data collected.")