import os
import requests

API_KEY = os.environ["SERPAPI_KEY"]
SCHOLAR_ID = os.environ["SCHOLAR_ID"]

params = {
    "engine": "google_scholar_author",
    "author_id": SCHOLAR_ID,
    "api_key": API_KEY,
    "hl": "en",
}

response = requests.get(
    "https://serpapi.com/search.json",
    params=params,
    timeout=30,
)

response.raise_for_status()
data = response.json()

# Google Scholar 总引用数
citations = data["cited_by"]["table"][0]["citations"]["all"]

with open("_data/scholar.yml", "w", encoding="utf-8") as f:
    f.write(f"citations: {citations}\n")

print(f"Google Scholar citations: {citations}")
