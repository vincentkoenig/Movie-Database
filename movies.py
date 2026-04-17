from movie_storage import movie_storage_sql as movie_storage
import movie_api
import statistics
import random
import difflib
import matplotlib.pyplot as plt

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

# Aktiver Nutzer
current_user = None


def select_user():
    """Nutzer auswählen oder neu erstellen."""
    global current_user
    print(f"{BLUE}\nWelcome to the Movie App! 🎬{RESET}")

    while True:
        users = movie_storage.get_all_users()
        print(f"\n{YELLOW}Select a user:{RESET}")
        for i, user in enumerate(users, 1):
            print(f"{YELLOW}{i}. {user['name']}{RESET}")
        print(f"{YELLOW}{len(users) + 1}. Create new user{RESET}")

        try:
            choice = int(input(f"{CYAN}Enter choice: {RESET}"))
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")
            continue

        if 1 <= choice <= len(users):
            current_user = users[choice - 1]
            print(f"{GREEN}Welcome back, {current_user['name']}! 🎬{RESET}")
            return
        elif choice == len(users) + 1:
            name = input(f"{CYAN}Enter new username: {RESET}").strip()
            if not name:
                print(f"{RED}Username cannot be empty!{RESET}")
                continue
            movie_storage.add_user(name)
            user_id = movie_storage.get_user_id(name)
            current_user = {"id": user_id, "name": name}
            print(f"{GREEN}User '{name}' created! Welcome! 🎬{RESET}")
            return
        else:
            print(f"{RED}Invalid choice.{RESET}")


def delete_user():
    """Löscht einen Nutzer und alle seine Filme."""
    users = movie_storage.get_all_users()
    if not users:
        print(f"{RED}No users found!{RESET}")
        return

    print(f"\n{YELLOW}Select a user to delete:{RESET}")
    for i, user in enumerate(users, 1):
        print(f"{YELLOW}{i}. {user['name']}{RESET}")

    try:
        choice = int(input(f"{CYAN}Enter choice: {RESET}"))
    except ValueError:
        print(f"{RED}Invalid input.{RESET}")
        return

    if 1 <= choice <= len(users):
        user = users[choice - 1]
        confirm = input(f"{RED}Delete '{user['name']}' and all their movies? (y/n): {RESET}").strip().lower()
        if confirm == "y":
            if user["id"] == current_user["id"]:
                print(f"{RED}You cannot delete the currently active user!{RESET}")
                return
            movie_storage.delete_user(user["id"])
            print(f"{GREEN}User '{user['name']}' successfully deleted!{RESET}")
    else:
        print(f"{RED}Invalid choice.{RESET}")


def list_of_movies():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}{current_user['name']}, your movie collection is empty. Add some movies!{RESET}")
        return
    print(f"{BLUE}\n{len(movies)} movies in total:{RESET}")
    for movie in movies:
        print(f"{GREEN}{movie['title']}: {movie['rating']}; Year: {movie['year']}{RESET}")


def add_a_movie():
    movie_input = input(f"{CYAN}Enter new movie name: {RESET}").strip()
    if not movie_input:
        print(f"{RED}Movie name cannot be empty!{RESET}")
        return

    movie_data = movie_api.fetch_movie_data(movie_input)
    if movie_data is None:
        return

    movies = movie_storage.get_movies(current_user["id"])
    for movie in movies:
        if movie["title"].lower() == movie_data["title"].lower():
            print(f"{RED}Movie '{movie_data['title']}' already exists!{RESET}")
            return

    movie_storage.add_movie(movie_data["title"], movie_data["year"],
                            movie_data["rating"], movie_data["poster"],
                            current_user["id"])
    print(f"{GREEN}Movie '{movie_data['title']}' added to {current_user['name']}'s collection!{RESET}")


def delete_a_movie():
    movies = movie_storage.get_movies(current_user["id"])
    movie_input = input(f"{CYAN}Enter movie name to delete: {RESET}").strip()
    for movie in movies:
        if movie["title"].lower() == movie_input.lower():
            movie_storage.delete_movie(movie_input, current_user["id"])
            print(f"{GREEN}Movie '{movie_input}' successfully deleted!{RESET}")
            return
    print(f"{RED}Movie '{movie_input}' doesn't exist!{RESET}")


def update_a_movie():
    movies = movie_storage.get_movies(current_user["id"])
    movie_input = input(f"{CYAN}Enter movie name to update: {RESET}").strip()
    for movie in movies:
        if movie["title"].lower() == movie_input.lower():
            try:
                rating_input = float(input(f"{CYAN}Enter new movie rating (0-10): {RESET}"))
            except ValueError:
                print(f"{RED}Invalid rating!{RESET}")
                return
            if 0 <= rating_input <= 10:
                movie_storage.update_movie(movie_input, rating_input, current_user["id"])
                print(f"{GREEN}Movie '{movie_input}' successfully updated!{RESET}")
            else:
                print(f"{RED}Rating must be between 0 and 10.{RESET}")
            return
    print(f"{RED}Movie '{movie_input}' doesn't exist!{RESET}")


def stats_of_movies():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return
    ratings = [movie["rating"] for movie in movies]
    print(f"{BLUE}Average rating: {statistics.mean(ratings):.1f}{RESET}")
    print(f"{BLUE}Median rating: {statistics.median(ratings):.1f}{RESET}")
    best_rating = max(ratings)
    best_movies = [m["title"] for m in movies if m["rating"] == best_rating]
    print(f"{GREEN}Best movie(s): {', '.join(best_movies)} ({best_rating:.1f}){RESET}")
    worst_rating = min(ratings)
    worst_movies = [m["title"] for m in movies if m["rating"] == worst_rating]
    print(f"{RED}Worst movie(s): {', '.join(worst_movies)} ({worst_rating:.1f}){RESET}")


def random_movie():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return
    movie = random.choice(movies)
    print(f"{BLUE}Your movie for tonight: {GREEN}{movie['title']}{BLUE}, "
          f"it's rated {movie['rating']:.1f}{RESET}")


def search_a_movie():
    movies = movie_storage.get_movies(current_user["id"])
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
            print(f"{RED}Did you mean:{RESET}")
            for title in similar:
                rating = next(m["rating"] for m in movies if m["title"] == title)
                print(f"{YELLOW}{title}, {rating:.1f}{RESET}")
        else:
            print(f"{RED}Movie not found.{RESET}")


def filter_movies():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return
    min_rating_input = input(f"{CYAN}Enter minimum rating (leave blank for none): {RESET}").strip()
    start_year_input = input(f"{CYAN}Enter start year (leave blank for none): {RESET}").strip()
    end_year_input = input(f"{CYAN}Enter end year (leave blank for none): {RESET}").strip()
    try:
        min_rating = float(min_rating_input) if min_rating_input else None
    except ValueError:
        min_rating = None
    try:
        start_year = int(start_year_input) if start_year_input else None
    except ValueError:
        start_year = None
    try:
        end_year = int(end_year_input) if end_year_input else None
    except ValueError:
        end_year = None
    filtered = [m for m in movies
                if (min_rating is None or m["rating"] >= min_rating)
                and (start_year is None or m["year"] >= start_year)
                and (end_year is None or m["year"] <= end_year)]
    if filtered:
        for movie in filtered:
            print(f"{GREEN}{movie['title']} ({movie['year']}): {movie['rating']:.1f}{RESET}")
    else:
        print(f"{RED}No movies match the criteria.{RESET}")


def sorted_by_rating():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return
    for movie in sorted(movies, key=lambda m: m["rating"], reverse=True):
        print(f"{GREEN}{movie['title']}: {movie['rating']:.1f}{RESET}")


def sorted_by_year():
    movies = movie_storage.get_movies(current_user["id"])
    if not movies:
        print(f"{RED}No movies in database!{RESET}")
        return
    while True:
        choice = input(f"{CYAN}Show newest first? (y/n): {RESET}").strip().lower()
        if choice in {"y", "n"}:
            break
        print(f"{RED}Please enter 'y' or 'n'.{RESET}")
    for movie in sorted(movies, key=lambda m: m["year"], reverse=(choice == "y")):
        print(f"{GREEN}{movie['title']}: {movie['rating']:.1f}; Year: {movie['year']}{RESET}")


def get_a_histogram():
    movies = movie_storage.get_movies(current_user["id"])
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


def generate_website():
    movies = movie_storage.get_movies(current_user["id"])
    movie_grid = ""
    for movie in movies:
        movie_grid += f"""
        <li>
            <div class="movie">
                <img class="movie-poster" src="{movie['poster']}" alt="{movie['title']}"/>
                <div class="movie-title">{movie['title']}</div>
                <div class="movie-year">{movie['year']}</div>
                <div class="movie-rating">⭐ {movie['rating']}</div>
            </div>
        </li>
        """
    with open("index_template.html", "r") as f:
        template = f.read()
    html = template.replace("__TEMPLATE_TITLE__", f"{current_user['name']}'s Movie App")
    html = html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)
    filename = f"{current_user['name']}.html"
    with open(filename, "w") as f:
        f.write(html)
    print(f"{GREEN}Website was generated successfully as {filename}{RESET}")


def switch_user():
    """Wechselt den aktiven Nutzer."""
    select_user()


def pause():
    input(f"{CYAN}\nPress Enter to continue...{RESET}")


def main():
    select_user()

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
        11: get_a_histogram,
        12: generate_website,
        13: switch_user,
        14: delete_user
    }

    while True:
        print(f"{BLUE}\n********** {current_user['name']}'s Movie Database **********{RESET}")
        print(f"{YELLOW}0. Exit{RESET}")
        for num, func in actions.items():
            print(f"{YELLOW}{num}. {func.__name__.replace('_', ' ').capitalize()}{RESET}")

        try:
            choice = int(input(f"{CYAN}\nEnter choice (0-14): {RESET}"))
        except ValueError:
            print(f"{RED}Please enter a valid number (0-14).{RESET}")
            continue

        if choice == 0:
            print("Bye!")
            return

        action = actions.get(choice)
        if action:
            action()
        else:
            print(f"{RED}Invalid choice.{RESET}")

        pause()


if __name__ == "__main__":
    main()