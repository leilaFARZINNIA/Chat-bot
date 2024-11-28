import csv

def read_csv_to_dict(file_name):
    dictionary = {}
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Kopfzeile überspringen (optional)
            next(reader)
            for row in reader:
                # Die erste Spalte ist die Frage, der Rest sind die Antworten
                question = row[0]
                answers = row[1:]
                dictionary[question] = answers
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_name}' wurde nicht gefunden. Bitte überprüfen Sie den Dateipfad.")
    except PermissionError:
        print(f"Fehler: Sie haben keine Berechtigung zum Lesen der Datei '{file_name}'.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    
    return dictionary
