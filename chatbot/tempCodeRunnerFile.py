from datetime import datetime


def format_message(sender, message):
    timestamp = datetime.now().strftime('%H:%M:%S')
    return f"{timestamp} {sender}: {message}"