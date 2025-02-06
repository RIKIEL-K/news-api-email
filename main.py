import requests
from send_email import send_email

API_Key = "c8b8e95bcc724a73a6a07f384a6992a1"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-01-06&sortBy=publishedAt&apiKey=c8b8e95bcc724a73a6a07f384a6992a1")
request = requests.get(url)
content = request.json()

msg=""
for article in content["articles"]:
       if article["title"] is not None and article["description"] is not None:
              msg = msg + article["title"]+ "\n" + article["description"] + 2*"\n"

msg = msg.encode('utf-8')
send_email(message=msg)