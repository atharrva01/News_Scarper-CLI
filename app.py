import requests
import argparse

parser = argparse.ArgumentParser(description="This is news scraper cli")
parser.add_argument("--query" , required = True , help = "Add the query here.")
args = parser.parse_args()

api = "xyz"  # as this API key has certain limits i am changing it so no one could access it , if you want add your own API key here

query = args.query

url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=us&max=10&apikey={api}"

data = requests.get(url).json()

if "articles" not in data or not data["articles"]:
    print("❌ No news articles found for this query.")
    exit()

print("Here are your Top 5 news: \n")

for i in data["articles"][:5]:
    print(f"The Title of the news is, {i['title']}\n")
    print(f"The description: \n{i['description']}\n")
    print(f"If you want to read the full article visit \n{i['url']}\n")
    print(f"This article is published at \n{i['publishedAt']}\n")

    
