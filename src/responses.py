import time
import random  
from multi_responsing import compuond_question
from answer_suggesting import word_in_questions
from file_handling import read_csv_to_dict

def get_welcome_message():
    return "Hallo!"

def get_opening_question():
    return "Wie kann ich Ihnen behilflich sein?"


def is_one_word(text):
    return ' ' not in text.strip() and len(text.strip()) > 0

def handle_input(user_input):

    predefined_answers = read_csv_to_dict("data/data.csv")
    
    # Das Gespräch zu Ende zu bringen
    if user_input.lower() == "bye":
        return None 
        
    elif is_one_word(user_input):
        word_in_questions(user_input, predefined_answers)
    else:
        return compuond_question(user_input, predefined_answers)
    
def get_current_time():
    return time.strftime("%H:%M:%S")

def print_message(sender, message):
    aktuelle_zeit = get_current_time()
    print(f"{aktuelle_zeit} {sender}: {message}")


def get_random_massage():

    begruessungen = ["Hallo!", "Guten Tag!", "Hey! Wie geht's?", "Hallo! Schön, dich hier zu sehen."]    

    fragen = ["Wie kann ich Ihnen heute helfen?", "Woran denken Sie gerade?", 
              "Gibt es etwas, bei dem ich Ihnen helfen kann?", "Wie war Ihr Tag bisher?"]

    # Zufällige Auswahl einer Begrüßung und einer Frage
    print_message("Chatbot", random.choice(begruessungen))
    print_message("Chatbot", random.choice(fragen))
