# Movie Database 🎬

A feature-rich command-line movie management app built with Python. Search any movie via the **OMDb API**, manage a personal collection per user, generate statistics, export a visual HTML website, and more.

## Demo

```
********** Vincent's Movie Database **********
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats of movies
6. Random movie
7. Search movie
8. Filter movies
9. Sorted by rating
10. Sorted by year
11. Histogram
12. Generate website
13. Switch user
14. Delete user

Enter choice (0-14):
```

## Features

- 🔍 **OMDb API integration** — add any movie by title; title, year, rating, poster, IMDb ID and country are fetched automatically
- 👥 **Multi-user support** — each user has their own separate movie collection stored in SQLite
- 📊 **Statistics** — average rating, median, best and worst movies in your collection
- 🔎 **Smart search** — substring match with fuzzy suggestions via `difflib` when no exact match is found
- 🎲 **Random recommendation** — get a random movie pick from your collection
- 🔧 **Filter & sort** — filter by minimum rating and year range; sort by rating or year (asc/desc)
- 📈 **Histogram** — generate and save a PNG rating distribution chart via Matplotlib
- 🌐 **HTML website generator** — export your collection as a styled webpage with movie posters, IMDb links, ratings, and country flag emojis
- 🗑️ **User management** — create, switch between, and delete users with full cascade deletion

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

- **Python 3.x**
- **SQLAlchemy** — ORM-based SQLite storage layer
- **requests** — OMDb API calls
- **python-dotenv** — secure API key management via `.env`
- **matplotlib** — rating histogram generation
- **difflib** — fuzzy movie title matching
- **statistics** — mean, median calculations

## Project Structure

```
Movie-Database/
├── movies.py               # Main app — CLI menu & all features
├── movie_api.py            # OMDb API integration
├── movie_storage/
│   └── movie_storage_sql.py # SQLAlchemy storage layer (users + movies)
├── index_template.html     # HTML template for website export
├── style.css               # Styling for generated website
├── requirements.txt        # Dependencies
├── .env                    # API key (not committed)
└── .gitignore
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Movie-Database.git
cd Movie-Database
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create a `.env` file with your OMDb API key**
```
API_KEY=your_api_key_here
```
> Get a free key at [omdbapi.com](http://www.omdbapi.com/)

**4. Run the app**
```bash
python movies.py
```

## Usage Examples

**Add a movie**
```
Enter new movie name: Inception
→ Movie 'Inception' added to Vincent's collection!
```

**Generate your personal website**
```
Enter choice: 12
→ Website was generated successfully as Vincent.html
```

**Search with fuzzy matching**
```
Enter part of movie name: Inceptoin
→ Did you mean:
  Inception, 8.8
```

## What I Learned

- Building a modular CLI application with a clean separation of concerns (UI / API / storage)
- Integrating a third-party REST API with secure key management using `python-dotenv`
- Designing a multi-user SQLite database with SQLAlchemy ORM
- Implementing fuzzy search with `difflib.get_close_matches`
- Generating dynamic HTML from a template using string replacement
- Creating and saving data visualizations with Matplotlib
- Converting country names to Unicode flag emojis programmatically
