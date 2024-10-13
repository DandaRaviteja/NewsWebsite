import requests

def get_telugu_news(api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'Telugu OR Andhra OR Telangana OR HYDERABAD',  # Query for Telugu news
        'language': 'te',  # Language code for Telugu
        'sortBy': 'publishedAt',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Raw JSON response:\n", data)  # Print raw JSON response
        articles = data.get('articles', [])
        if articles:
            for article in articles:
                print(f"Title: {article['title']}")
                print(f"Description: {article['description']}")
                print(f"URL: {article['url']}\n")
        else:
            print("No articles found.")
    else:
        print(f"Failed to retrieve news: {response.status_code}")

if __name__ == "__main__":
    api_key = '935f9b8078d941c688ce9605ba80bac4'  # Replace with your actual News API key
    get_telugu_news(api_key)
