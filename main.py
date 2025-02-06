import requests
from send_email import send_email

topic = "tesla"
API_Key = "c8b8e95bcc724a73a6a07f384a6992a1"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-01-06&sortBy=publishedAt&apiKey=c8b8e95bcc724a73a6a07f384a6992a1&language=en"
request = requests.get(url)
content = request.json()

msg="Subject: Today's news \n\n"
for article in content["articles"][:20]:
       if article["title"] is not None and article["description"] is not None:
              msg += article["title"]+ "\n" + article["description"] + article["url"] +2*"\n"

msg = msg.encode('utf-8')
send_email(message=msg)