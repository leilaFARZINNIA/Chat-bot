import random
import logging
from file_handling import load_questions_from_csv

def display_visual_feedback(is_correct):
    """
    Zeigen Sie das visuelle Symbol ✅ oder ❌ basierend auf der Antwort des Benutzers an.
    """
    if is_correct:
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")

def play_game(file_name="data/questions.csv"):
    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info(f"Log info: Quiz started")
        
    questions = load_questions_from_csv(file_name)
    random.shuffle(questions)
    total_questions = 10
    score = 0

    print("Trivia game activated! Type 'exit' anytime to quit.")

    for i, question_dict in enumerate(questions[:total_questions]):
        print(f"\nQuestion {i + 1} of {total_questions}: {question_dict['question']}")
        for idx, choice in enumerate(question_dict['choices']):
            print(f"  {idx + 1}. {choice}")

        user_input = input("\nYour answer (1-4) or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print(f"Game exited. Your final score is {score}/{total_questions}.")
            return

        try:
            user_answer = int(user_input) - 1
            if question_dict['choices'][user_answer].strip() == question_dict['correct_answer'].strip():
                display_visual_feedback(True)  #Zeigen Sie das Symbol ✅ für die richtige Antwort an.
            else:
                display_visual_feedback(False)  # Zeigen Sie das Symbol ❌ für die falsche Antwort an.
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")

        print(f"Progress: Question {i + 1} of {total_questions}; Score: {score}/{total_questions}")

    print(f"\nGame over! Your final score is {score}/{total_questions}.")