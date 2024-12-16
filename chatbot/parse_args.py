import argparse
import random
from utils import format_message

from responses import handle_input, get_random_massage
from read_data import add_answer, read_csv_to_dict, remove_answer, write_dict_to_csv, validate_data, add_question, remove_question,load_questions_from_csv

def start_quiz(file_name="questions.csv", num_questions=10):
    questions = load_questions_from_csv(file_name)
    
    if not questions:
        print("Keine Fragen im CSV-Dateiformat gefunden.")
        return
    
    score = 0
    random.shuffle(questions)  
    
    print("Das Quiz-Spiel startet! Viel Spaß!")
    
    for i, question in enumerate(questions[:num_questions]):
        print(f"Frage {i + 1}: {question['question']}")
        for idx, choice in enumerate(question['choices'], start=1):
            print(f"{idx}. {choice}")
        
        answer = input("Geben Sie Ihre Antwort ein (1-4), oder 'exit' zum Verlassen: ")
        
        if answer.lower() == 'exit':
            print("Sie haben das Spiel verlassen.")
            break
        
        if question['choices'][int(answer) - 1] == question['correct_answer']:
            print("Richtig!")
            score += 1
        else:
            print(f"Falsch! Die richtige Antwort ist: {question['correct_answer']}")
        
        print()  # Zeilenumbruch zwischen den Fragen

    print(f"Spiel beendet! Ihr Punktestand ist: {score}/{num_questions}")



def list_questions(file_name="data.csv"):
    knowledge_base = read_csv_to_dict(file_name)
    
    print("Fragen in der Wissensbasis:")
    for index, question in enumerate(knowledge_base.keys(), start=1):
        print(f"{index}. {question}")

def parsing_args():

    parser = argparse.ArgumentParser(description="Chatbot Konsole App")
    parser.add_argument("--question", type=str, help="Stellen Sie direkt eine Frage")
    parser.add_argument("--list-questions", "-q", action="store_true", help="Zeigt alle Fragen aus der Wissensbasis an")
    parser.add_argument("--importing", action="store_true", help="Flagge zum Importieren neuer Daten und Ersetzen der bestehenden Wissensbasis")
    parser.add_argument("--filetype", choices=["CSV"], help="Dateityp (derzeit wird nur CSV unterstützt)")
    parser.add_argument("--newfile", help="Pfad zur neuen zu importierenden CSV-Datei")
    parser.add_argument("--outputfile", help="Pfad zum Speichern der aktualisierten CSV-Datei (new_data.csv)")
    parser.add_argument("--add", action="store_true", help="Add a new answer to an existing question or add a new question with an answer.")
    parser.add_argument("--remove", action="store_true", help="Remove a specific answer from a question.")
    parser.add_argument("--question-for-edit", type=str, help="The question to modify.")
    parser.add_argument("--answer-for-adit", type=str, help="The answer to add or remove.")
    parser.add_argument("--add-question", type=str, help="The question to modify.")
    parser.add_argument("--remove-question", type=str, help="The question remove.")
    parser.add_argument("--start-quiz", action="store_true", help="Startet das Quiz-Spiel.")
    parser.add_argument("--exit", action="store_true", help="Beendet das Quiz-Spiel während des Spiels.")




    args = parser.parse_args()

    try:

        csv_data = "data.csv"
     

        # Load the existing data
        data_as_dictionary = read_csv_to_dict(csv_data)

        if args.add and args.add_question:
            add_question(data_as_dictionary, csv_data, args.add_question, args.answer_for_adit)
            return "adding-question"
        
        elif args.remove and args.remove_question:
            remove_question(data_as_dictionary, csv_data, args.remove_question)
            return "removing-question"

        elif args.add and args.question_for_edit:
            add_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "adding-answer"
        
        elif args.remove and args.question_for_edit:
            remove_answer(data_as_dictionary, csv_data, args.question_for_edit, args.answer_for_adit)
            return "removing-answer"

        elif args.list_questions:
            list_questions()
            return "list-questions"

        elif args.question:
            response = handle_input(args.question)
            if response: print(format_message("Chatbot", response))

            return "commandline-ask"
        
        elif args.start_quiz:
            print("Ein Quiz-Spiel beginnt!")
            start_quiz()
            return "start-quiz"
        
        elif args.exit:
            print("Das Spiel wurde beendet.")
            return "exit-quiz"
        
        
        elif args.importing and args.filetype == "CSV":
            new_data = read_csv_to_dict(args.newfile)
            if new_data and validate_data(new_data):
                write_dict_to_csv(args.outputfile, new_data)
                return "importing-file"
        else:
            get_random_massage()
            return "nothing"
        
       
    
    except Exception as e:
        print(f"An error occurred: {e}")