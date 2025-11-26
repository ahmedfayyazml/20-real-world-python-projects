import requests

from send_email import send_email

api_key = "568de588371843c09f4f66260cb4cab6"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-10-26"
       "&sortBy=publishedAt&apiKey=568de588371843c09f4f66260cb4cab6")
#make requests
request = requests.get(url)
#get a dictionary with data
content = request.json()


#access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = (body + article["title"]+"\n"
                +article["description"]+"\n"+
                article["url"]+2*"\n")
body = body.encode("utf-8")
send_email(message=body)