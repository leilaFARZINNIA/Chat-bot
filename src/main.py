import logging
from utils.formats import format_message
from parse_args import parsing_args
from responses import handle_input

def main():

    returned_value = parsing_args()

    # if(returned_value == "importing-file" or returned_value == None
    #    or returned_value == "adding-answer" or returned_value == "removing-answer"
    #    or returned_value == "removing-question" or returned_value == "adding-question"): return
    # print("returned_value: ", returned_value)


    if(not (returned_value == "nothing" or returned_value == "commandline-ask")): return


    while True:
        user_input = input(format_message("Benutzer", "")).strip()
        response = handle_input(user_input)

        if response is None: break

        print(format_message("Chatbot", response))


def exit_app():
    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info("Log info: App exited.\n")

if __name__ == "__main__":
    main()
    exit_app()