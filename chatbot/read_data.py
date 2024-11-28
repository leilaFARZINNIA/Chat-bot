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



def write_dict_to_csv(file_path, data):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Ensures all fields are quoted
            # Schreiben Sie die Kopfzeile
            writer.writerow(["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"])
            
            for question, answers in data.items():
                # Füllen Sie fehlende Antworten mit leeren Zeichenfolgen, wenn es weniger als 5 Antworten gibt
                answers = answers + [''] * (5 - len(answers))  # Stellen Sie sicher, dass es 5 Spalten für Antworten gibt
                writer.writerow([question] + answers)
        
        print(f"Daten erfolgreich in {file_path} geschrieben")
    
    except Exception as e:
        print(f"Fehler beim Schreiben in die CSV-Datei: {e}")



def validate_data(new_data):
    if len(new_data) < 10:
        print("Fehler: Neue Daten müssen mindestens 10 Fragen enthalten.")
        return False
    return True