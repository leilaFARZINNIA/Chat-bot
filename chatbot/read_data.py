import csv
import os
import traceback
from datetime import datetime


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
    except FileNotFoundError as e:
        log_error(e)
        print(f"Fehler: Die Datei '{file_name}' wurde nicht gefunden. Bitte überprüfen Sie den Dateipfad.")
    except PermissionError as e:
        log_error(e)
        print(f"Fehler: Sie haben keine Berechtigung zum Lesen der Datei '{file_name}'.")
    except Exception as e:
        log_error(e)
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    
    return dictionary


def validate_data(new_data):
    if len(new_data) < 10:
        print("Fehler: Neue Daten müssen mindestens 10 Fragen enthalten.")
        return False
    return True


def write_dict_to_csv(file_path, dictionary_data):
    try:
        validate_file_path(file_path)
        
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Stellt sicher, dass alle Felder angegeben werden
            # Schreib die Kopfzeile
            writer.writerow(["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"])
            
            for question, answers in dictionary_data.items():
                # Füll fehlende Antworten mit leeren Zeichenfolgen, wenn es weniger als 5 Antworten gibt
                answers = answers + [''] * (5 - len(answers))  # Stell sicher, dass es 5 Spalten für Antworten gibt
                writer.writerow([question] + answers)
        
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        log_error(e)
        print(f"Error writing to CSV file: {e}")

def validate_file_path(file_path):
    try:
        # Prüf, ob die Datei eine .csv-Erweiterung hat
        if not file_path.lower().endswith('.csv'):
            raise ValueError("The file must have a .csv extension.")

        # Prüf die Existenz von Verzeichnissen und Schreibberechtigungen
        directory = os.path.dirname(file_path) or '.'  # Aktuelles Verzeichnis als Standard behandeln
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory {directory} does not exist.")
        if not os.access(directory, os.W_OK):
            raise PermissionError(f"Write permission denied for the directory {directory}.")

    except Exception as e:
        log_error(e)
        raise

def log_error(exception):
    # Sicherstellen, dass das Verzeichnis logs existiert
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Speichere das Traceback-log
    traceback_file = os.path.join(log_dir, f"traceback_{timestamp}.log")
    with open(traceback_file, mode='w', encoding='utf-8') as tb_file:
        tb_file.write(traceback.format_exc())
    print(f"Traceback saved to {traceback_file}")

    # Speichere ein Chat-log Zusammenfassung
    chat_log_file = os.path.join(log_dir, f"chat_log_{timestamp}.log")
    with open(chat_log_file, mode='w', encoding='utf-8') as chat_file:
        chat_file.write(f"Timestamp: {timestamp}\n")
        chat_file.write(f"Error: {str(exception)}\n")
    print(f"Chat log saved to {chat_log_file}")