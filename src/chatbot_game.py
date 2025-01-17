import random
import logging
from file_handling import load_questions_from_csv

def play_game(file_name="data/questions.csv"):

    if logging.getLogger().isEnabledFor(logging.INFO):
        logging.info(f"Log info: Quiz started")
        
    questions = load_questions_from_csv(file_name)

    random.shuffle(questions)
    total_questions = 10
    score = 0

    print("Trivia game activated! Type 'exit' anytime to quit.")

    progressIndicator = ""
    percentIndicator = 0
    for i, question_dict in enumerate(questions[:total_questions]):
        print(f"\nQuestion {i + 1} of {total_questions}: {question_dict['question']}")
        progressIndicator = progressIndicator+f"*****"
        percentIndicator = percentIndicator + 10
        print(progressIndicator, f"{percentIndicator}%")

        for idx, choice in enumerate(question_dict['choices']):
            print(f"  {idx + 1}. {choice}")

        user_input = input("\nYour answer (1-4) or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print(f"Game exited. Your final score is {score}/{total_questions}.")
            return

        try:
            
            user_answer = int(user_input) - 1
            if question_dict['choices'][user_answer].strip() == question_dict['correct_answer'].strip():
                print(f"✅ Richtig! Your answer: {question_dict['correct_answer']}")
                score += 1
            else:
                print(f"❌ Falsch! The correct answer was: {question_dict['correct_answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")

        print(f"Progress: Question {i + 1} of {total_questions}; Score: {score}/{total_questions}")

    print(f"\nGame over! Your final score is {score}/{total_questions}.")