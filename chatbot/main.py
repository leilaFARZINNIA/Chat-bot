from utils import format_message
from parse_args import parsing_args
from responses import handle_input

def main():

    parsing_args()

    while True:
        user_input = input(format_message("Benutzer", "")).strip()
        response = handle_input(user_input)

        if response is None:
            print(format_message("Chatbot", "bye"))
            break
        print(format_message("Chatbot", response))


if __name__ == "__main__":
    main()
