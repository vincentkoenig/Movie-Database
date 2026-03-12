# Movie-Database

Eine einfache **Film-Datenbank als Command Line Interface (CLI)**, geschrieben in Python.  
Das Programm ermöglicht es, Filme zu speichern, zu verwalten und nach verschiedenen Kriterien zu analysieren.

Dieses Projekt ist Teil meines Lernwegs zum **AI / Software Engineer**.

---

## Features

- Filme hinzufügen
- Filme löschen
- Bewertung eines Films aktualisieren
- Alle Filme anzeigen
- Filme nach Bewertung sortieren
- Filme chronologisch sortieren
- Zufälligen Film auswählen
- Filme suchen
- Filme filtern (nach Bewertung und Zeitraum)
- Statistiken berechnen
- Histogramm der Bewertungen erstellen

---

## Funktionsweise

Die Filme werden in einer **JSON-Datei (`movies.json`) gespeichert**.

Beispielstruktur:

```json
{
  "Titanic": {
    "rating": 9,
    "year": 1997
  },
  "Inception": {
    "rating": 8.8,
    "year": 2010
  }
}

## Projektstruktur
movie-project/
│
├── main.py
├── movie_storage.py
├── movies.json
└── README.md

## Dateien

main.py

Steuert das gesamte Programm und die Benutzerinteraktion.

movie_storage.py

Kümmert sich um:

Laden der Filme

Speichern der Filme

Hinzufügen

Löschen

Aktualisieren

movies.json

Speichert die Filmdaten.

⚙️ Installation
1️⃣ Python installieren

Falls Python noch nicht installiert ist:

https://www.python.org/downloads/

2️⃣ Projekt klonen
git clone https://github.com/vincentkoenig/movie-database.git

oder herunterladen.

3️⃣ Abhängigkeiten installieren

Das Projekt nutzt:

matplotlib

Installation:

pip install matplotlib
▶️ Projekt starten

Navigiere in den Projektordner und starte:

python main.py
🖥️ Menü im Programm
********** My Movies Database **********

1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Filter movies
9. Sort by rating
10. Sort by year
11. Generate histogram
0. Exit
📊 Beispiel Funktionen
Filme filtern

Du kannst Filme filtern nach:

Mindestbewertung

Startjahr

Endjahr

Beispiel:

Enter minimum rating: 8
Enter start year: 2000
Enter end year:
Chronologische Sortierung

Der Nutzer kann entscheiden:

Show newest movies first? (y/n)
📈 Histogramm der Bewertungen

Das Programm kann automatisch ein Diagramm erstellen:

ratings_histogram.png
