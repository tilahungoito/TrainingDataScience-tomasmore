import requests
import pandas as pd

# 🔐 Replace with your API key from https://newsdata.io
API_KEY = "pub_937308483d6841c3a0da13fa0e3f8991"

# Using newsdata.io API endpoint
url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&language=en"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data.get("results", [])

    # Extract important fields
    news_data = []
    for article in articles:
        # newsdata.io uses different field names:
        source = article.get("source_id") or article.get("source_name")
        
        author = article.get("creator")
        if isinstance(author, list):
            author = ", ".join(author)
            
        published_at = article.get("pubDate")
        # Format the date so it contains a 'T' to satisfy the regex parsing in our Jupyter notebook
        # '2026-03-05 04:30:57' -> '2026-03-05T04:30:57Z'
        if published_at and " " in published_at:
            published_at = published_at.replace(" ", "T") + "Z"

        news_data.append({
            "source": source,
            "author": author,
            "title": article.get("title"),
            "description": article.get("description"),
            "publishedAt": published_at
        })

    df = pd.DataFrame(news_data)

    # Save dataset
    df.to_csv("news_data.csv", index=False)

    print("Data saved successfully to news_data.csv!")
    print(df.head())
else:
    print(f"Error fetching data: {response.status_code}")
    print(response.text)
