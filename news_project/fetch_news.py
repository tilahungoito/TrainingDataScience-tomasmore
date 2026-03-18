import requests
import pandas as pd

# 🔐 Replace with your API key from https://newsdata.io
API_KEY = "pub_937308483d6841c3a0da13fa0e3f8991"

# Using newsdata.io API endpoint
def fetch_news(api_key, max_pages=60):
    all_articles = []
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}&language=en"
    
    current_page: int = 0
    while url and current_page < max_pages:
        print(f"Fetching page {current_page + 1}...")
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get("results", [])
            all_articles.extend(articles)
            
            # Get the next page token
            next_page = data.get("nextPage")
            if next_page:
                url = f"https://newsdata.io/api/1/latest?apikey={api_key}&language=en&page={next_page}"
            else:
                url = None
                
            current_page += 1
        else:
            print(f"Error fetching data: {response.status_code}")
            print(response.text)
            break
            
    return all_articles

articles = fetch_news(API_KEY) # Using default max_pages=60 from function signature

if articles:
    # Extract important fields
    news_data = []
    for article in articles:
        source = article.get("source_id") or article.get("source_name")
        
        author = article.get("creator")
        if isinstance(author, list):
            author = ", ".join(author)
            
        published_at = article.get("pubDate")
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

    print(f"Data saved successfully to news_data.csv! Total articles: {len(df)}")
    print(df.head())
else:
    print("No articles fetched. Check your API key and connection.")
