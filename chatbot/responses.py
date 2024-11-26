from datetime import datetime
import time
import random  

def get_welcome_message():
    return "Hallo!"

def get_opening_question():
    return "Wie kann ich Ihnen behilflich sein?"

#پاسخ های هر مقدار به لیست تبدیل شد
predefined_answers = {
    "Wie heißt du?": ["I am Chatbot."],
    "Wie funktioniert diese App?": ["Sie Stellen Fragen und ich antworte"],
    "Wie spät ist es?": [f"Es ist {datetime.now().strftime('%H:%M:%S')} Uhr."],
    "Wie geht es dir?": ["Es geht mir gut, bis deinem Computer gut geht."],
    "Was ist dein Zweck?": ["Ich bin hier um dir zu helfen."],
    "Wer hat dich entwickelt?": ["Ich wurde von Project9 Teammitgelider entwickelt."],
    "Kannst du mir einen Witz erzählen?": ["Sorry nein, aktuell kann ich dir keinen Witz erzählen"],
    "Was ist dein Lieblingstier?": ["Mein Lieblingstier ist Pfau"],
    "Hast du einen Lieblingsfilm?": ["Ich mag alle Filme von Jacki chan"],
    "Wo wohnst du?": ["Ich wohne in jeder Computer, der mich installiert hat"],
    "Kannst du tanzen?": ["Sehr gut, hahaha"],
    "Was ist deine Lieblingsfarbe?": ["Meine Lieblingsfarbe sind Blau and Grun"],
    "wie geht es dir?": ["Mir geht es gut, danke!"],
    "was ist dein name?": ["Mein Name ist Chatbot."],
    "Wie funktioniert diese App?": [
        "Diese App hilft Ihnen bei Ihren Fragen.",
        "Stellen Sie eine Frage, und ich werde versuchen zu antworten.",
        "Ich bin hier, um Ihnen Informationen zu geben.",
        "Ich kann viele Fragen beantworten. Probieren Sie es aus!"
    ],
    "Wie heißt du?": [
        "Ich heiße Chatbot.",
        "Nennen Sie mich einfach Bot.",
        "Ich bin Ihr virtueller Assistent.",
        "Mein Name ist Chatbot, schön Sie kennenzulernen!"
    ],
    "Wie geht es dir?": [
        "Mir geht es gut, danke der Nachfrage.",
        "Ich fühle mich großartig!",
        "Alles läuft perfekt hier.",
        "Danke, mir geht's wunderbar!"
    ]
}



def handle_input(user_input):
    if user_input.lower() == "bye":
        return None  # Das Gespräch zu Ende zu bringen
    elif user_input in predefined_answers:
        # return predefined_answers[user_input]
        possible_answers = predefined_answers[user_input]
        return random.choice(possible_answers)
    else:
        return "Es tut mir leid, ich kenne diese Frage nicht. Bitte Stelle Sie eine andere Frage."
    
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
