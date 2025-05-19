
import requests

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def search_wikipedia(query):
    params = {
        "action": "query", 
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query
    }

    try:
        response = requests.get(WIKI_API_URL, params=params).json()
        pages = response.get("query", {}).get("pages", {})
        if not pages:
            return "No Wikipedia summary found."
        page = next(iter(pages.values()))
        return page.get("extract", "No content found.")
    except Exception as e:
        return f"Error fetching Wikipedia: {e}"
