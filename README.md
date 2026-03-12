# 🎬 Movie Database (Python CLI Project)

Eine einfache **Film-Datenbank als Command Line Interface (CLI)**, geschrieben in Python.  
Das Programm ermöglicht es, Filme zu speichern, zu verwalten und nach verschiedenen Kriterien zu analysieren.

Dieses Projekt ist Teil meines Lernwegs zum **AI / Software Engineer**.

---

## 🚀 Features

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

## 🧠 Funktionsweise

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

Jeder Film enthält:

Titel

Bewertung

Erscheinungsjahr

Die Daten werden beim Start des Programms geladen und nach Änderungen wieder gespeichert.

📂 Projektstruktur
movie-database/
│
├── main.py
├── movie_storage.py
├── movies.json
└── README.md
Dateien

main.py

Steuert das gesamte Programm und die Benutzerinteraktion über ein Menü im Terminal.

movie_storage.py

Kümmert sich um:

Laden der Filme aus der JSON-Datei

Speichern der Filme

Hinzufügen neuer Filme

Löschen von Filmen

Aktualisieren von Bewertungen

movies.json

Speichert dauerhaft alle Filmdaten.

⚙️ Installation
1️⃣ Python installieren

Falls Python noch nicht installiert ist:

https://www.python.org/downloads/

2️⃣ Repository klonen
git clone https://github.com/vincentkoenig/movie-database.git

oder das Repository als ZIP herunterladen.

3️⃣ Abhängigkeiten installieren

Das Projekt nutzt Matplotlib für die Erstellung eines Histogramms.

Installation:

pip install matplotlib
▶️ Projekt starten

Navigiere im Terminal in den Projektordner und starte das Programm:

python main.py
🖥️ Menü im Programm

Nach dem Start erscheint ein Menü im Terminal:

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

Der Nutzer kann eine Zahl eingeben, um die gewünschte Funktion auszuführen.

🔎 Beispiel Funktionen
Filme filtern

Filme können nach folgenden Kriterien gefiltert werden:

Mindestbewertung

Startjahr

Endjahr

Beispiel:

Enter minimum rating (leave blank for no minimum rating): 8
Enter start year (leave blank for no start year): 2000
Enter end year (leave blank for no end year):
Chronologische Sortierung

Der Nutzer kann entscheiden, ob:

die neuesten Filme zuerst

oder die ältesten Filme zuerst

angezeigt werden.

Show newest movies first? (y/n)
Zufälliger Film

Das Programm kann auch einen zufälligen Film aus der Datenbank auswählen:

Your movie for tonight: Inception, it's rated 8.8
📊 Histogramm der Bewertungen

Mit Hilfe von Matplotlib kann ein Diagramm erstellt werden, das die Verteilung der Bewertungen zeigt.

Das Bild wird automatisch gespeichert, zum Beispiel als:

ratings_histogram.png
