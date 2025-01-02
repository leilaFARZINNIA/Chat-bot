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
        epilog="""Beispiele:""")

    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    parser.add_argument("--answer", type=str, help="The answer to add or remove.")

    parser.add_argument("--add-question", action="store_true", help="Add a question")
    parser.add_argument("--remove-question", action="store_true", help="Remove a question")
    parser.add_argument("--add-answer", action="store_true", help="Add a new answer to a question or add a new question with an answer")
    parser.add_argument("--remove-answer", action="store_true", help="Remove a specific answer")

    parser.add_argument("--list-questions", "-q", action="store_true", help="List questions")

    parser.add_argument("--importing", action="store_true", help="Importing from CSV file")
    parser.add_argument("--filet-ype", choices=["CSV"], help="CSV Type")
    parser.add_argument("--from-csv", help="Reading from a path")
    parser.add_argument("--to-csv", help="Writing to a path")

    parser.add_argument("--start-game", action="store_true", help="A simple game")
 
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

        if args.add_question and args.question:
            add_question(data_as_dictionary, csv_data, args.question, args.answer)
            return "adding-question"
        
        elif args.remove_question and args.question:
            remove_question(data_as_dictionary, csv_data, args.question)
            return "removing-question"

        elif args.add_answer and args.question:
            add_answer(data_as_dictionary, csv_data, args.question, args.answer)
            return "adding-answer"
        
        elif args.remove_answer and args.question and args.answer:
            remove_answer(data_as_dictionary, csv_data, args.question, args.answer)
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
        
        elif args.importing and args.filet_ype == "CSV":
            new_data = read_csv_to_dict(args.from_csv)
            if new_data and validate_data(new_data):
                write_dict_to_csv(args.to_csv, new_data)
                return "importing-file"
        else:
            get_random_massage()
            return "nothing"
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    # else:
    #     print("❌ Fehler: Ungültige Eingabe oder kein Argument angegeben.")
    #     parser.print_help()
    #     return "show-help"