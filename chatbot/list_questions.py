import argparse

knowledge_base = [
    "Wie ist das Wetter heute?",
    "Was ist deine Lieblingsfarbe?",
    "Wie spät ist es?",
    "Erzähl mir einen Witz.",
    "Wie lautet dein Name?"
]

def list_questions(debug=False):
    if debug:
        print("Debug Mode aktiviert. Fragen werden angezeigt...")
    
    print("Fragen in der Wissensbasis:")
    for index, question in enumerate(knowledge_base, start=1):
        print(f"{index}. {question}")

def main():
    # Konfiguration von argparse zum Verarbeiten von Befehlszeilenargumenten
    parser = argparse.ArgumentParser(description="ChatBot Service Provider Tool")
    parser.add_argument(
        "--list-questions",
        "-q",
        action="store_true",
        help="Zeigt alle internen Fragen aus der Wissensbasis an"
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Aktiviert den Debug-Modus"
    )
    
    # Verarbeitung der Befehlszeilenargumente
    args = parser.parse_args()
    
    if args.list_questions:
        list_questions(debug=args.debug)
    else:
        print("Verwenden Sie --list-questions oder -q, um alle Fragen anzuzeigen.")

if __name__ == "__main__":
    main()
