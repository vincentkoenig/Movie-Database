import json
import os

MOVIES_FILE = "movies.json"


def get_movies():
    """Lädt die Filme aus der JSON-Datei und gibt sie als Liste zurück."""
    if not os.path.exists(MOVIES_FILE):
        return []  # Leere Liste, wenn Datei noch nicht existiert
    with open(MOVIES_FILE, "r") as f:
        try:
            data = json.load(f)
            # Daten von dict zu Liste konvertieren
            movies = []
            for title, info in data.items():
                movies.append({
                    "title": title,
                    "year": info["year"],
                    "rating": info["rating"]
                })
            return movies
        except json.JSONDecodeError:
            return []  # Leere Liste, wenn JSON kaputt ist


def save_movies(movies):
    """Speichert die Liste von Filmen in der JSON-Datei."""
    data = {movie["title"]: {"year": movie["year"], "rating": movie["rating"]} for movie in movies}
    with open(MOVIES_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_movie(title, year, rating):
    """Fügt einen Film hinzu und speichert die Daten."""
    movies = get_movies()
    movies.append({"title": title, "year": year, "rating": rating})
    save_movies(movies)


def delete_movie(title):
    """Löscht einen Film und speichert die Daten."""
    movies = get_movies()
    movies = [movie for movie in movies if movie["title"].lower() != title.lower()]
    save_movies(movies)


def update_movie(title, rating):
    """Aktualisiert die Bewertung eines Films und speichert die Daten."""
    movies = get_movies()
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["rating"] = rating
            break
    save_movies(movies)
