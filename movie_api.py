import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "http://www.omdbapi.com/"

def fetch_movie_data(title):
    """Ruft Filmdaten von der OMDb API ab."""
    response = requests.get(API_URL, params={"apikey": API_KEY, "t": title})
    data = response.json()

    if data.get("Response") == "False":
        print(f"Movie '{title}' not found on OMDb!")
        return None

    return {
        "title": data["Title"],
        "year": int(data["Year"]),
        "rating": float(data["imdbRating"]),
        "poster": data["Poster"],
        "imdb_id": data["imdbID"],
        "country": data.get("Country", "").split(",")[0].strip()
    }