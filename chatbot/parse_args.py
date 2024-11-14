import argparse

from utils import format_message
from responses import handle_input, get_random_massage

def parsing_args():

    # Erstellen eines Parsers für Befehlszeilenargumente
    parser = argparse.ArgumentParser(description="Chatbot Konsole App")
    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    args = parser.parse_args()
 
    if args.question:
        response = handle_input(args.question)
        if response:
            print(format_message("Chatbot", response))
        else:
            print(format_message("Chatbot", "bye"))
        return
    else:
        get_random_massage()
