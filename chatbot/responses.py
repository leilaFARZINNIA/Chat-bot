from datetime import datetime

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
    "Was ist deine Lieblingsfarbe?": "Meine Lieblingsfarbe sind Blau and Grun"
}


def handle_input(user_input):
    if user_input.lower() == "bye":
        return None  # Das Gespräch zu Ende zu bringen
    elif user_input in predefined_answers:
        return predefined_answers[user_input]
    # return f"Sie habe gesagt: {user_input}"
    else:
        return "Es tut mir leid, ich kenne diese Frage nicht. Bitte Stelle Sie eine andere Frage."