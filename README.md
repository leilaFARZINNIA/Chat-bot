# Anleitung

## Virtuelle Umgebung erstellen und verwenden

```bash
python3 -m venv path/to/venv
```
Dieser Befehl wird verwendet, um eine virtuelle Umgebung (Virtual Environment) in Python zu erstellen.

```bash
source path/to/venv/bin/activate
```
Dieser Befehl wird verwendet, um eine virtuelle Python-Umgebung (Virtual Environment) zu aktivieren.

```bash
python3 -m pip install pytest
```
Der Befehl wird verwendet, um das Python-Paket pytest zu installieren.

```bash
pytest tests/
```
Dieser Befehl führt die Tests in einem Verzeichnis namens `tests/` aus.

```bash
deactivate
```
Dieser Befehl bringt dich zurück in die normale Systemumgebung.

---

## Fragen und Antworten verwalten

### Frage hinzufügen
```bash
python3 src/main.py --add-question --question "Frage A" --answer "Antwort 1"
```

### Frage entfernen
```bash
python3 src/main.py --remove-question --question "Frage A"
```

### Antwort hinzufügen
```bash
python3 src/main.py --add-answer --question "Frage A" --answer "Antwort A 1"
```

### Antwort entfernen
```bash
python3 src/main.py --remove-answer --question "Frage A" --answer "Antwort A 1"
```

### Fragen auflisten
```bash
python3 src/main.py --list-questions
```

---

## Daten aus einer CSV-Datei importieren
```bash
python3 src/main.py --importing --file-type CSV --from-csv from/dir/file.csv --to-csv to/dir/file.csv
```

---

## Spiel starten
```bash
python3 src/main.py --start-game
```

---

## Wetteranalyse durchführen
```bash
python3 src/main.py --weather --city Braunschweig --days 3
```

---

## Alle Dateien gleichzeitig testen
```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## Neue Projekte innerhalb des aktuellen Projekts

Zwei zusätzliche Projekte wurden in das aktuelle Projektverzeichnis aufgenommen:
1. **chatbot-ui**: Die Web- und Mobile-UI mit Expo.
2. **chatbot-server**: Der Server mit FastAPI, Python, PyMongo und Uvicorn.

### Server starten
```bash
cd chatbot-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### UI starten
```bash
cd chatbot-ui
npm install
npx expo start
```

