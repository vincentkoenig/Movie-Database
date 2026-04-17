# 🎬 Meine Filmdatenbank

Eine Kommandozeilen-Anwendung zur Verwaltung deiner persönlichen Filmsammlung, unterstützt durch die OMDb API und SQLite.

## Funktionen
- Filme automatisch über die OMDb API hinzufügen (Titel, Jahr, Bewertung, Poster)
- Filme auflisten, suchen, filtern und sortieren
- Statistiken anzeigen (Durchschnitt, Median, bester, schlechtester Film)
- Visuelle HTML-Website aus der Sammlung generieren
- Zufällige Filmempfehlung

## Einrichtung

### 1. Repository klonen
\`\`\`sh
git clone <deine-repo-url>
cd Filmdatenbank
\`\`\`

### 2. Abhängigkeiten installieren
\`\`\`sh
pip install -r requirements.txt
\`\`\`

### 3. `.env` Datei mit deinem OMDb API-Schlüssel erstellen
\`\`\`
API_KEY=dein_api_key_hier
\`\`\`
Kostenlosen API-Schlüssel erhalten auf [omdbapi.com](http://www.omdbapi.com/)

## Verwendung
\`\`\`sh
python movies.py
\`\`\`

## Projektstruktur
\`\`\`
Filmdatenbank/
├── movies.py              # Hauptanwendung
├── movie_storage_sql.py   # SQLite-Speicherschicht
├── movie_api.py           # OMDb API-Integration
├── index_template.html    # HTML-Vorlage für Website-Generierung
├── style.css              # CSS-Styling
├── requirements.txt       # Abhängigkeiten
├── .env                   # API-Schlüssel (nicht in Git)
└── .gitignore
\`\`\`

## Abhängigkeiten
Siehe `requirements.txt`. Verwendete Bibliotheken:
- `sqlalchemy` – Datenbankverwaltung
- `requests` – API-Anfragen
- `python-dotenv` – Umgebungsvariablen
- `matplotlib` – Histogramm-Generierung