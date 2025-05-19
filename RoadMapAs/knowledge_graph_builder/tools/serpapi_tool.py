import os 
from dotenv import load_dotenv
import requests
SERP_API_KEY = os.getenv("SERP_API_KEY")


def search_google(query):
    url= f"http://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
    return requests.get(url).json().get("orqanic_result",[])
