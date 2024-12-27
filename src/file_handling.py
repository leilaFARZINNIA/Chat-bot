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
        
        print(f"Daten erfolgreich geschrieben in {file_path}")
    except Exception as e:
        log_error(e)
        print(f"Fehler beim Schreiben in eine CSV-Datei: {e}")

def validate_file_path(file_path):
    try:
        # Prüf, ob die Datei eine .csv-Erweiterung hat
        if not file_path.lower().endswith('.csv'):
            raise ValueError("Die Datei muss eine .csv-Erweiterung haben.")

        # Prüf die Existenz von Verzeichnissen und Schreibberechtigungen
        directory = os.path.dirname(file_path) or '.'  # Aktuelles Verzeichnis als Standard behandeln
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Das Verzeichnis {directory} existiert nicht.")
        if not os.access(directory, os.W_OK):
            raise PermissionError(f"Schreibberechtigung für das Verzeichnis verweigert {directory}.")

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

def add_answer(data_as_dictionary, file_path, question, new_answer):
    try:
        # Wenn die Frage bereits im Wörterbuch vorhanden ist
        if question in data_as_dictionary:
            # Suchen Sie die erste leere Stelle (""), und setzen Sie die neue Antwort dort ein
            for i in range(len(data_as_dictionary[question])):
                if data_as_dictionary[question][i] == "":
                    data_as_dictionary[question][i] = new_answer
                    break
        else:
            # Wenn die Frage nicht vorhanden ist, erstellen Sie einen neuen Eintrag mit der neuen Antwort
            data_as_dictionary[question] = [new_answer] + [""] * 4  # Füll den Rest mit leeren Strings

        # Stellen Sie sicher, dass keine Frage mehr als 5 Antworten hat
        for key in data_as_dictionary:
            # Die Liste auf maximal 5 Antworten kürzen, ggf. mit leeren Zeichenfolgen auffüllen
            data_as_dictionary[key] = data_as_dictionary[key][:5] + [''] * (5 - len(data_as_dictionary[key]))

        # Schreiben des aktualisierten Wörterbuchs zurück in die CSV-Datei
        write_dict_to_csv(file_path, data_as_dictionary)
        print(f"Erfolgreich wurde die Antwort '{new_answer}' in der Frage '{question}' hinzugefügt.")

    except Exception as e:
        print(f"Fehler beim Hinzufügen der Antwort: {e}")


def remove_answer(data_as_dictionary, file_path, question, answer_to_remove):
    try:
        if question not in data_as_dictionary:
            raise ValueError(f"Die Frage '{question}' existiert nich.")

        if answer_to_remove not in data_as_dictionary[question]:
            raise ValueError(f"Die Antwort '{answer_to_remove}' gibt es nich für Frage '{question}'.")

        data_as_dictionary[question].remove(answer_to_remove)

        # Sicherstellen, dass alle Zeilen genau 5 Antworten haben
        for key in data_as_dictionary:
            data_as_dictionary[key] = data_as_dictionary[key][:5] + [''] * (5 - len(data_as_dictionary[key]))

        write_dict_to_csv(file_path, data_as_dictionary)
        print(f"Die Antwort '{answer_to_remove}' wurde erfolgreich aus der Frage '{question}' entfernt.")

    except Exception as e:
        log_error(e)
        print(f"Fehler beim Entfernen der Antwort: {e}")


# dic = { question1: [a1, a2] }

def add_question(data_as_dictionary, file_path, question, new_answer):
    add_answer(data_as_dictionary, file_path, question, new_answer)

def remove_question(data_as_dictionary, file_path, question):
    try:
    
        if (data_as_dictionary[question]):
            del data_as_dictionary[question]

        write_dict_to_csv(file_path, data_as_dictionary)
        print(f"Die Frage '{question}' wurde erfolgreich aus Dictionary entfernt.")

    except Exception as e:
        log_error(e)
        print(f"Fehler beim Entfernen der Antwort: {e}")


def load_questions_from_csv(file_name):
    questions = []
    
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question = {
                'question': row['question'],
                'choices': [row['choice1'], row['choice2'], row['choice3'], row['choice4']],
                'correct_answer': row['correct_answer']
            }
            questions.append(question)
    
    return questions
