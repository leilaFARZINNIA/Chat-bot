
from chatbot.responses import get_welcome_message, get_opening_question, handle_input, predefined_answers

def test_get_welcome_message():
    assert get_welcome_message() == "Hallo!"

def test_get_opening_question():
    assert get_opening_question() == "Wie kann ich Ihnen behilflich sein?"

def test_handle_input():
    # Testing questions
    assert handle_input("bye") is None
    for question in predefined_answers:
        assert handle_input(question) == predefined_answers[question]

def test_handle_input_unrecognized_question():
    # Testing unrecognized questions
    assert handle_input("Wie ist das Wetter?") == "Es tut mir leid, ich kenne diese Frage nicht. Bitte Stelle Sie eine andere Frage."
