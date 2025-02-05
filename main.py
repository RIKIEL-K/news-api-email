import requests


API_Key = "c8b8e95bcc724a73a6a07f384a6992a1"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-01-05&"
       "sortBy=publishedAt&apiKey=c8b8e95bcc724a73a6a07f384a6992a1")
request = requests.get(url)
content = request.json()

print(content["articles"])