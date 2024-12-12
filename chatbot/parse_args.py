import argparse
from utils import format_message

from responses import handle_input, get_random_massage
from read_data import add_answer, read_csv_to_dict, remove_answer, write_dict_to_csv, validate_data

def list_questions(file_name="data.csv"):
    knowledge_base = read_csv_to_dict(file_name)
    
    print("Fragen in der Wissensbasis:")
    for index, question in enumerate(knowledge_base.keys(), start=1):
        print(f"{index}. {question}")

def parsing_args():

    parser = argparse.ArgumentParser(description="Chatbot Konsole App")
    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    parser.add_argument("--list-questions", "-q", action="store_true", help="Zeigt alle Fragen aus der Wissensbasis an")
    parser.add_argument("--importing", action="store_true", help="Flagge zum Importieren neuer Daten und Ersetzen der bestehenden Wissensbasis")
    parser.add_argument("--filetype", choices=["CSV"], help="Dateityp (derzeit wird nur CSV unterstützt)")
    parser.add_argument("--newfile", help="Pfad zur neuen zu importierenden CSV-Datei")
    parser.add_argument("--outputfile", help="Pfad zum Speichern der aktualisierten CSV-Datei (new_data.csv)")
    parser.add_argument("--add", action="store_true", help="Add a new answer to an existing question or add a new question with an answer.")
    parser.add_argument("--remove", action="store_true", help="Remove a specific answer from a question.")
    parser.add_argument("--question-for-edit", type=str, required=True, help="The question to modify.")
    parser.add_argument("--answer-for-adit", type=str, required=True, help="The answer to add or remove.")

    args = parser.parse_args()

    try:

        csv_data = "data.csv"

        # Load the existing data
        data_as_dictionary = read_csv_to_dict(csv_data)

        if args.add:
            add_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "adding-answer"
        
        elif args.remove:
            remove_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "removing-answer"

        elif args.list_questions:
            list_questions()
            return "list-questions"

        elif args.question:
            response = handle_input(args.question)
            if response: print(format_message("Chatbot", response))

            return "commandline-ask"
        
        elif args.importing and args.filetype == "CSV":
            new_data = read_csv_to_dict(args.newfile)
            if new_data and validate_data(new_data):
                write_dict_to_csv(args.outputfile, new_data)
                return "importing-file"
        else:
            get_random_massage()
            return "nothing"
    
    except Exception as e:
        print(f"An error occurred: {e}")