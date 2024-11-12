from chatbot.utils import format_message
import re

def test_format_message():
    message = format_message("Chatbot", "Hallo!")
    
    # Test that the message contains the correct format with timestamp and message
    assert re.match(r"\d{2}:\d{2}:\d{2} Chatbot: Hallo!", message)