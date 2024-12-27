import random
import logging

from read_data import load_questions_from_csv

def start_quiz(file_name="data/questions.csv", num_questions=10):
    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info(f"Log info: Quiz started")

    try:
       
        questions = load_questions_from_csv(file_name)
        
        if not questions:
            print("⚠️ Keine Fragen im CSV-Dateiformat gefunden.")
            return
        
        print("\n🎮 Willkommen zum Quiz-Spiel! Viel Spaß! 🎉\n")
        
        score = 0  
        random.shuffle(questions)  
        
        
        for i, question in enumerate(questions[:num_questions]):
            print(f"Frage {i + 1}: {question['question']}")
            for idx, choice in enumerate(question['choices'], start=1):
                print(f"  {idx}. {choice}")
            
            
            while True:
                answer = input("\n📝 Geben Sie Ihre Antwort (1-4), oder 'exit' zum Verlassen ein: ").strip()
                if answer.lower() == 'exit':  
                    print("\n🚪 Sie haben das Spiel verlassen. Danke fürs Spielen!")
                    print(f"🎯 Ihr Punktestand bis jetzt: {score}/{i + 1}\n")
                    return
                elif answer.isdigit() and 1 <= int(answer) <= 4:  
                    break
                else:
                    print("❌ Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")
            
            
            chosen_answer = question['choices'][int(answer) - 1]
            if chosen_answer == question['correct_answer']:
                print("✅ Richtig!")
                score += 1
            else:
                print(f"❌ Falsch!")
            
            
            print(f"🔍 Die richtige Antwort ist: {question['correct_answer']}")
            print()
        
        
        print(f"🎉 Spiel beendet! Ihr Punktestand ist: {score}/{num_questions}\n")
        if score == num_questions:
            print("🏆 Perfekt! Sie haben alle Fragen richtig beantwortet!")
        elif score > num_questions // 2:
            print("👏 Gut gemacht! Versuchen Sie, noch besser zu werden.")
        else:
            print("💡 Übung macht den Meister! Probieren Sie es noch einmal.")
    
    except Exception as e:
        print(f"❌ Ein Fehler ist aufgetreten: {e}")