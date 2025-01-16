from datetime import datetime


def format_message(sender, message):
    timestamp = datetime.now().strftime('%H:%M:%S')
    return f"{timestamp} {sender}: {message}"


def current_formated_date():
    
    current_date = datetime.today()
    return current_date.strftime("%Y-%m-%d") # YYYY-MM-DD