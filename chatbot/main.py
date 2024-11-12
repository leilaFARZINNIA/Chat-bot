import argparse
from utils import format_message
from responses import get_welcome_message, get_opening_question, handle_input


def main():
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

    print(format_message("Chatbot", get_welcome_message()))
    print(format_message("Chatbot", get_opening_question()))

    while True:
        user_input = input(format_message("Benutzer", "")).strip()
        response = handle_input(user_input)

        if response is None:
            print(format_message("Chatbot", "bye"))
            break
        print(format_message("Chatbot", response))


if __name__ == "__main__":
    main()
