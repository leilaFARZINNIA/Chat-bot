import random 

def word_in_questions(keyword, questions):

    # Fragen filtern, die das Schlüsselwort enthalten
    matching_questions = [q for q in questions if keyword.lower() in q.lower()]

    # Prüfen Sie, ob es passende Fragen gibt
    if not matching_questions:
        print("Keine passenden Fragen für das Stichwort gefunden.")
        return

    # Anzeige der passenden Fragen als nummerierte Liste
    print("Passende Fragen:")
    for i, question in enumerate(matching_questions, start=1):
        print(f"{i}. {question}")

    # Benutzerauswahl abrufen
    try:
        choice = int(input("\nWählen Sie eine Frage nach Nummer: "))
        if 1 <= choice <= len(matching_questions):
            selected_question = matching_questions[choice - 1]
            print(f"\nAntworten für '{selected_question}':")
            # for idx, answer in enumerate(questions[selected_question], start=1):
            #     print(f"{idx}. {answer}")
            print(random.choice(questions[selected_question]))
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine gültige Nummer.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
