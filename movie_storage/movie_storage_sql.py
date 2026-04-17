from sqlalchemy import create_engine, text

DB_URL = "sqlite:///data/movies.db"
engine = create_engine(DB_URL, echo=False)

with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """))
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL,
            poster TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """))
    connection.commit()


def get_all_users():
    """Gibt alle Nutzer zurück."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, name FROM users"))
        return [{"id": row[0], "name": row[1]} for row in result.fetchall()]


def add_user(name):
    """Fügt einen neuen Nutzer hinzu."""
    with engine.connect() as connection:
        try:
            connection.execute(text("INSERT INTO users (name) VALUES (:name)"),
                               {"name": name})
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")


def get_user_id(name):
    """Gibt die ID eines Nutzers zurück."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id FROM users WHERE name = :name"),
                                    {"name": name})
        row = result.fetchone()
        return row[0] if row else None


def delete_user(user_id):
    """Löscht einen Nutzer und alle seine Filme."""
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM movies WHERE user_id = :user_id"),
                           {"user_id": user_id})
        connection.execute(text("DELETE FROM users WHERE id = :user_id"),
                           {"user_id": user_id})
        connection.commit()

def get_movies(user_id):
    """Gibt alle Filme eines Nutzers zurück."""
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT title, year, rating, poster FROM movies WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        return [{"title": row[0], "year": row[1], "rating": row[2], "poster": row[3]}
                for row in result.fetchall()]


def add_movie(title, year, rating, poster, user_id):
    """Fügt einen Film für einen bestimmten Nutzer hinzu."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("INSERT INTO movies (title, year, rating, poster, user_id) "
                     "VALUES (:title, :year, :rating, :poster, :user_id)"),
                {"title": title, "year": year, "rating": rating,
                 "poster": poster, "user_id": user_id}
            )
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")


def delete_movie(title, user_id):
    """Löscht einen Film eines bestimmten Nutzers."""
    with engine.connect() as connection:
        connection.execute(
            text("DELETE FROM movies WHERE title = :title AND user_id = :user_id"),
            {"title": title, "user_id": user_id}
        )
        connection.commit()


def update_movie(title, rating, user_id):
    """Aktualisiert die Bewertung eines Films eines bestimmten Nutzers."""
    with engine.connect() as connection:
        connection.execute(
            text("UPDATE movies SET rating = :rating "
                 "WHERE title = :title AND user_id = :user_id"),
            {"rating": rating, "title": title, "user_id": user_id}
        )
        connection.commit()