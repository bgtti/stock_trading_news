import requests
from datetime import datetime

def get_news(API_KEY, company_name):
    response = requests.get(
        url=f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}")
    response.raise_for_status()
    articles = response.json()["articles"]
    three_articles = articles[:3] # http://stackoverflow.com/questions/509211/understanding-slice-notation
    articles_list = [
        [f"{article['title']}", f"{article['publishedAt']}", f"{article['description']}", f"{article['url']}"] for article in three_articles]
    for i in range(len(articles_list)):
        the_date = articles_list[i][1][:10]
        articles_list[i][1] = datetime.strptime(
            the_date, "%Y-%m-%d").strftime("%d %B, %Y")
    
    return articles_list
