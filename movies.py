import movie_storage
import statistics
import random
import difflib
import matplotlib.pyplot as plt  # Drittanbieter-Import am Ende

# ------------------- Farben -------------------
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

# ------------------- Funktionen -------------------
def list_of_movies():
    """Listet alle Filme mit Bewertung und Jahr auf."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    print(f"{BLUE}\n{len(movies)} movies in total:{RESET}")
    for movie in movies:
        print(f"{GREEN}{movie['title']}: {movie['rating']}; Year: {movie['year']}{RESET}")


def add_a_movie():
    """Fügt einen neuen Film in die JSON-Datenbank hinzu, wenn er noch nicht existiert."""
    movies = movie_storage.get_movies()

    movie_input = input(f"{CYAN}Enter new movie name: {RESET}").strip()
    if not movie_input:
        print(f"{RED}Movie name cannot be empty!{RESET}")
        return

    # Prüfen, ob der Film bereits existiert
    for movie in movies:
        if movie["title"].lower() == movie_input.lower():
            print(f"{RED}Movie '{movie_input}' already exists!{RESET}")
            return

    # Rating abfragen
    try:
        rating_input = float(input(f"{CYAN}Enter new movie rating (0-10): {RESET}"))
        if not 0 <= rating_input <= 10:
            print(f"{RED}Rating must be between 0 and 10.{RESET}")
            return
    except ValueError:
        print(f"{RED}Invalid rating! Must be a number between 0 and 10.{RESET}")
        return

    # Release Year abfragen
    try:
        year_input = int(input(f"{CYAN}Enter the year of release: {RESET}"))
    except ValueError:
        print(f"{RED}Invalid year! Must be a number.{RESET}")
        return

    # Film hinzufügen
    movie_storage.add_movie(movie_input, year_input, rating_input)
    print(f"{GREEN}Movie '{movie_input}' successfully added!{RESET}")


def delete_a_movie():
    """Löscht einen Film, wenn er existiert."""
    movies = movie_storage.get_movies()
    movie_input = input(f"{CYAN}Enter movie name to delete: {RESET}").strip()

    for movie in movies:
        if movie["title"].lower() == movie_input.lower():
            movie_storage.delete_movie(movie_input)
            print(f"{GREEN}Movie '{movie_input}' successfully deleted!{RESET}")
            return
    print(f"{RED}Movie '{movie_input}' doesn't exist!{RESET}")


def update_a_movie():
    """Aktualisiert die Bewertung eines existierenden Films."""
    movies = movie_storage.get_movies()
    movie_input = input(f"{CYAN}Enter movie name to update: {RESET}").strip()

    for movie in movies:
        if movie["title"].lower() == movie_input.lower():
            try:
                rating_input = float(input(f"{CYAN}Enter new movie rating (0-10): {RESET}"))
            except ValueError:
                print(f"{RED}Invalid rating! Must be a number between 0 and 10.{RESET}")
                return
            if 0 <= rating_input <= 10:
                movie_storage.update_movie(movie_input, rating_input)
                print(f"{GREEN}Movie '{movie_input}' successfully updated!{RESET}")
            else:
                print(f"{RED}Rating must be between 0 and 10.{RESET}")
            return
    print(f"{RED}Movie '{movie_input}' doesn't exist!{RESET}")


def stats_of_movies():
    """Zeigt Durchschnitt, Median, besten und schlechtesten Film an."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    ratings = [movie["rating"] for movie in movies]
    print(f"{BLUE}Average rating: {statistics.mean(ratings):.1f}{RESET}")
    print(f"{BLUE}Median rating: {statistics.median(ratings):.1f}{RESET}")

    best_rating = max(ratings)
    best_movies = [movie["title"] for movie in movies if movie["rating"] == best_rating]
    print(f"{GREEN}Best movie(s): {', '.join(best_movies)} ({best_rating:.1f}){RESET}")

    worst_rating = min(ratings)
    worst_movies = [movie["title"] for movie in movies if movie["rating"] == worst_rating]
    print(f"{RED}Worst movie(s): {', '.join(worst_movies)} ({worst_rating:.1f}){RESET}")


def random_movie():
    """Wählt zufällig einen Film aus."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    movie = random.choice(movies)
    print(f"{BLUE}Your movie for tonight: {GREEN}{movie['title']}{BLUE}, "
          f"it's rated {movie['rating']:.1f}{RESET}")


def search_a_movie():
    """Sucht nach Filmen anhand eines Namens oder Teils davon."""
    movies = movie_storage.get_movies()
    movie_input = input(f"{CYAN}Enter part of movie name: {RESET}").strip()
    found = False

    for movie in movies:
        if movie_input.lower() in movie["title"].lower():
            print(f"{GREEN}{movie['title']}, {movie['rating']:.1f}{RESET}")
            found = True

    if not found:
        titles = [movie["title"] for movie in movies]
        similar = difflib.get_close_matches(movie_input, titles, n=5, cutoff=0.6)
        if similar:
            print(f"{RED}The movie '{movie_input}' does not exist. Did you mean:{RESET}")
            for title in similar:
                rating = next(movie["rating"] for movie in movies if movie["title"] == title)
                print(f"{YELLOW}{title}, {rating:.1f}{RESET}")
        else:
            print(f"{RED}The movie '{movie_input}' does not exist "
                  f"and no similar movies were found.{RESET}")


def filter_movies():
    """Filtert Filme nach Mindestbewertung und Zeitraum."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    min_rating_input = input(f"{CYAN}Enter minimum rating (leave blank for no minimum rating): {RESET}").strip()
    start_year_input = input(f"{CYAN}Enter start year (leave blank for no start year): {RESET}").strip()
    end_year_input = input(f"{CYAN}Enter end year (leave blank for no end year): {RESET}").strip()

    try:
        min_rating = float(min_rating_input) if min_rating_input else None
    except ValueError:
        print(f"{RED}Invalid rating input. Ignoring minimum rating.{RESET}")
        min_rating = None

    try:
        start_year = int(start_year_input) if start_year_input else None
    except ValueError:
        print(f"{RED}Invalid start year input. Ignoring start year.{RESET}")
        start_year = None

    try:
        end_year = int(end_year_input) if end_year_input else None
    except ValueError:
        print(f"{RED}Invalid end year input. Ignoring end year.{RESET}")
        end_year = None

    filtered_movies = [
        movie for movie in movies
        if (min_rating is None or movie["rating"] >= min_rating)
        and (start_year is None or movie["year"] >= start_year)
        and (end_year is None or movie["year"] <= end_year)
    ]

    if filtered_movies:
        print(f"{BLUE}\nFiltered Movies:{RESET}")
        for movie in filtered_movies:
            print(f"{GREEN}{movie['title']} ({movie['year']}): {movie['rating']:.1f}{RESET}")
    else:
        print(f"{RED}No movies match the given criteria.{RESET}")


def sorted_by_rating():
    """Sortiert Filme nach Bewertung absteigend."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    for movie in sorted(movies, key=lambda m: m["rating"], reverse=True):
        print(f"{GREEN}{movie['title']}: {movie['rating']:.1f}{RESET}")


def sorted_by_year():
    """Zeigt die Filme chronologisch sortiert an."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    while True:
        choice = input(f"{CYAN}Show newest movies first? (y/n): {RESET}").strip().lower()
        if choice in {"y", "n"}:
            break
        print(f"{RED}Please enter 'y' or 'n'.{RESET}")
    reverse_order = choice == "y"

    for movie in sorted(movies, key=lambda m: m["year"], reverse=reverse_order):
        print(f"{GREEN}{movie['title']}: {movie['rating']:.1f}; Year: {movie['year']}{RESET}")


def get_a_histogram():
    """Erstellt ein Histogramm der Filmratings und speichert es als Bild."""
    movies = movie_storage.get_movies()
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return

    ratings = [movie["rating"] for movie in movies]
    plt.hist(ratings, bins=10, range=(0, 10), edgecolor="black")
    plt.title("Histogram of Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")

    filename = input(f"{CYAN}Enter filename to save histogram: {RESET}")
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        filename += ".png"

    plt.savefig(filename)
    plt.close()
    print(f"{GREEN}Histogram saved as {filename}{RESET}")


def pause():
    """Pause, bis der Benutzer Enter drückt."""
    input(f"{CYAN}\nPress Enter to continue...{RESET}")


# ------------------- Hauptprogramm -------------------
def main():
    actions = {
        1: list_of_movies,
        2: add_a_movie,
        3: delete_a_movie,
        4: update_a_movie,
        5: stats_of_movies,
        6: random_movie,
        7: search_a_movie,
        8: filter_movies,
        9: sorted_by_rating,
        10: sorted_by_year,
        11: get_a_histogram
    }

    while True:
        print(f"{BLUE}\n********** My Movies Database **********{RESET}")
        print(f"{YELLOW}0. Exit{RESET}")
        for num, func in actions.items():
            print(f"{YELLOW}{num}. {func.__name__.replace('_', ' ').capitalize()}{RESET}")

        try:
            choice = int(input(f"{CYAN}\nEnter choice (0-11): {RESET}"))
        except ValueError:
            print(f"{RED}Please enter a valid number (0-11).{RESET}")
            continue

        if choice == 0:
            print("Bye!")
            return

        action = actions.get(choice)
        if action:
            action()
        else:
            print(f"{RED}Invalid choice, please try again{RESET}")

        pause()


if __name__ == "__main__":
    main()
