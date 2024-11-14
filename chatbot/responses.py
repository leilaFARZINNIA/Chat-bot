from datetime import datetime
import time
import random  # Importieren des Zufallsmoduls für zufällige Auswahl

def get_welcome_message():
    return "Hallo!"

def get_opening_question():
    return "Wie kann ich Ihnen behilflich sein?"


predefined_answers = {
    "Wie heißt du?": "I am Chatbot.",
    "Wie funktioniert diese App?": "Sie Stellen Fragen und ich antworte",
    "Wie spät ist es?": f"Es ist {datetime.now().strftime('%H:%M:%S')} Uhr.",
    "Wie geht es dir?": "Es geht mir gut, bis deinem Computer gut geht.",
    "Was ist dein Zweck?": "Ich bin hier um dir zu helfen.",
    "Wer hat dich entwickelt?": "Ich wurde von Project9 Teammitgelider entwickelt.",
    "Kannst du mir einen Witz erzählen?": "Sorry nein, aktuell kann ich dir keinen Witz erzählen",
    "Was ist dein Lieblingstier?": "Mein Lieblingstier ist Pfau",
    "Hast du einen Lieblingsfilm?": "Ich mag alle Filme von Jacki chan",
    "Wo wohnst du?": "Ich wohne in jeder Computer, der mich installiert hat",
    "Kannst du tanzen?": "Sehr gut, hahaha",
    "Was ist deine Lieblingsfarbe?": "Meine Lieblingsfarbe sind Blau and Grun",
    "wie geht es dir?": "Mir geht es gut, danke!",
    "was ist dein name?": "Mein Name ist Chatbot."
}


def handle_input(user_input):
    if user_input.lower() == "bye":
        return None  # Das Gespräch zu Ende zu bringen
    elif user_input in predefined_answers:
        return predefined_answers[user_input]
    # return f"Sie habe gesagt: {user_input}"
    else:
        return "Es tut mir leid, ich kenne diese Frage nicht. Bitte Stelle Sie eine andere Frage."
    
def get_current_time():
    # Funktion zum Abrufen der aktuellen Uhrzeit im Format HH:MM:SS
    return time.strftime("%H:%M:%S")

def print_message(sender, message):
    # Funktion zum Anzeigen einer Nachricht mit Uhrzeit, Sender und Nachrichtentext
    aktuelle_zeit = get_current_time()
    print(f"{aktuelle_zeit} {sender}: {message}")


def get_random_massage():
    # Liste mit Begrüßungen auf Deutsch
    begruessungen = ["Hallo!", "Guten Tag!", "Hey! Wie geht's?", "Hallo! Schön, dich hier zu sehen."]
    
    # Liste mit Einstiegsfragen auf Deutsch
    fragen = ["Wie kann ich Ihnen heute helfen?", "Woran denken Sie gerade?", 
              "Gibt es etwas, bei dem ich Ihnen helfen kann?", "Wie war Ihr Tag bisher?"]

    # Zufällige Auswahl einer Begrüßung und einer Frage
    print_message("Chatbot", random.choice(begruessungen))
    print_message("Chatbot", random.choice(fragen))
