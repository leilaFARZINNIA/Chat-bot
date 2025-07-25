import logging
from api.api_call import get_sensor_data
from weather import calculate_average_temperature, respond_to_user_query
from utils.formats import current_formated_date, format_message
from args_parsing import parsing_args
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

        if(response and isinstance(response, list) and len(response[1]) > 0):
            print(format_message("Chatbot", f"{response[0]} \n{respond_to_user_query(response[1][0], current_formated_date())}"))

            print("Die durchschnittliche Temperatur im Inneren des Gebäudes beträgt: ", calculate_average_temperature(get_sensor_data(), "2025-01-16"))

        else: print(format_message("Chatbot", response))
            

def exit_app():
    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info("Log info: App exited.\n")

if __name__ == "__main__":
    main()
    exit_app()