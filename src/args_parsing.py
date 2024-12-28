import argparse
import logging

from chatbot_game import play_game
from utils.formats import format_message
from utils.logging import setup_logging
from responses import handle_input, get_random_massage
from file_handling import add_answer, read_csv_to_dict, remove_answer, write_dict_to_csv, validate_data, add_question, remove_question,load_questions_from_csv


def list_questions(file_name="data/data.csv"):
    knowledge_base = read_csv_to_dict(file_name)
    
    print("Fragen in der Wissensbasis:")
    for index, question in enumerate(knowledge_base.keys(), start=1):
        print(f"{index}. {question}")

def parsing_args():

    parser = argparse.ArgumentParser(
        description="Chatbot Konsole App: Ein Tool für Quiz, Fragenmanagement und CSV-Import.",
        epilog="""Beispiele:
    python main.py --list-questions         Zeigt alle Fragen an
    python main.py --add-question "Frage"   Fügt eine neue Frage hinzu
    python main.py --start-quiz             Startet das Quiz-Spiel
    python main.py --remove-question "Frage" Entfernt eine Frage"""
    )

    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    parser.add_argument("--list-questions", "-q", action="store_true", help="Zeigt alle Fragen aus der Wissensbasis an")
    parser.add_argument("--importing", action="store_true", help="Flagge zum Importieren neuer Daten und Ersetzen der bestehenden Wissensbasis")
    parser.add_argument("--filetype", choices=["CSV"], help="Dateityp (derzeit wird nur CSV unterstützt)")
    parser.add_argument("--newfile", help="Pfad zur neuen zu importierenden CSV-Datei")
    parser.add_argument("--outputfile", help="Pfad zum Speichern der aktualisierten CSV-Datei new_data.csv")
    parser.add_argument("--add", action="store_true", help="Add a new answer to an existing question or add a new question with an answer.")
    parser.add_argument("--remove", action="store_true", help="Remove a specific answer from a question.")
    parser.add_argument("--question-for-edit", type=str, help="The question to modify.")
    parser.add_argument("--answer-for-adit", type=str, help="The answer to add or remove.")
    parser.add_argument("--add-question", type=str, help="The question to modify.")
    parser.add_argument("--remove-question", type=str, help="The question remove.")
    parser.add_argument("--start-game", action="store_true", help="Startet das Quiz-Spiel.")
 
    # New logging arguments
    parser.add_argument('--log', action='store_true', help='Enable logging')
    parser.add_argument('--log-level', choices=['INFO', 'WARNING'], default='WARNING', help='Set log level')


    args = parser.parse_args()

    # Setup logging based on the arguments
    setup_logging(args.log, args.log_level)

    try:

        if args.log:
            logging.info('App started in logging mode.')

        csv_data = "data/data.csv"
     

        # Load the existing data
        data_as_dictionary = read_csv_to_dict(csv_data)

        if args.add and args.add_question:
            add_question(data_as_dictionary, csv_data, args.add_question, args.answer_for_adit)
            return "adding-question"
        
        elif args.remove and args.remove_question:
            remove_question(data_as_dictionary, csv_data, args.remove_question)
            return "removing-question"

        elif args.add and args.question_for_edit:
            add_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "adding-answer"
        
        elif args.remove and args.question_for_edit:
            remove_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "removing-answer"

        elif args.list_questions:
            list_questions()
            return "list-questions"

        elif args.question:
            response = handle_input(args.question)
            if response: print(format_message("Chatbot", response))

            return "commandline-ask"
        
        elif args.start_game:
            play_game()
            return "start-game"
        
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
        
    else:
        print("❌ Fehler: Ungültige Eingabe oder kein Argument angegeben.")
        parser.print_help()
        return "show-help"