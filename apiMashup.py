import requests
import json
import google.generativeai as genai

API_KEY = "AIzaSyBOu1Ek1fNT9spoXr9T14i4eSex0DMnklw"
newsAPI = "400c5c6276e54d7eb8b844d75ea05491"
country = "india"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsAPI}"

def fetch_news():
    result = requests.get(url)
    return result.json()

def summarize_news(data):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')  # Note: Changed to 'gemini-pro'

    news_texts = []
    for article in data["articles"][:5]:  # Limit to top 5 news items
        news_texts.append(f"Title: {article['title']}\nDescription: {article['description']}")

    prompt = "Summarize the following news in five concise points:\n\n" + "\n\n".join(news_texts)

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    news_data = fetch_news()
    summary = summarize_news(news_data)
    print(summary)

if __name__ == "__main__":
    main()