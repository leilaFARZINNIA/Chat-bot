import argparse

from utils import format_message
from responses import handle_input, get_random_massage

# Funktion zur Generierung der Antwort basierend auf der Frage
# def antwort_generieren(question, antworten_dict):
    # Antwort aus dem Wörterbuch holen oder Standardnachricht zurückgeben
#    return antworten_dict.get(question.lower(),"Entschuldigung, ich habe deine Frage nicht verstanden.")

def parsing_args():
    # Wörterbuch mit Fragen und Antworten
    #antworten_dict = {
    #    "wie geht es dir?": "Mir geht es gut, danke!",
    #    "was ist dein name?": "Mein Name ist Chatbot.",
        
    #}

    # Erstellen eines Parsers für Befehlszeilenargumente
    # parser = argparse.ArgumentParser(description="Chatbot Command Line Interface")
    parser = argparse.ArgumentParser(description="Chatbot Konsole App")
    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    args = parser.parse_args()

    # Definieren des Arguments --question
    # parser.add_argument('--question', type=str, help='Die Frage, die vom Chatbot verarbeitet werden soll')

    # Argumente verarbeiten
    # args = parser.parse_args()

    # Überprüfen, ob das Argument --question vorhanden ist
    # if args.question:
    #    # Antwort für die eingegebene Frage generieren
    #    antwort = antwort_generieren(args.question, antworten_dict)
    #    print(antwort)
    # else:
        # Wenn keine Frage vorhanden ist, wird eine Willkommensnachricht angezeigt
    #    print("Willkommen beim Chatbot! Bitte geben Sie Ihre Frage ein.")
 
    if args.question:
        response = handle_input(args.question)
        if response:
            print(format_message("Chatbot", response))
        else:
            print(format_message("Chatbot", "bye"))
        return
    else:
        get_random_massage()
    
# Ausführen der Hauptfunktion
#if __name__ == "__main__":
#   main()
