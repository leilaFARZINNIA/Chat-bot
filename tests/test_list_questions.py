import unittest
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chatbot.list_questions import list_questions

class TestListQuestions(unittest.TestCase):
    # Test für die Ausgabe von list_questions ohne Debug-Modus
    def test_list_questions_output(self):
        # Umleiten der Standardausgabe zu einem StringIO-Objekt für den Test
        captured_output = StringIO()
        sys.stdout = captured_output

        # Aufruf der Funktion ohne Debug-Modus
        list_questions(debug=False)

        # Wiederherstellen der Standardausgabe
        sys.stdout = sys.__stdout__

        # Erwartete Ausgabe ohne Debug-Modus
        expected_output = "Fragen in der Wissensbasis:\n"
        for index, question in enumerate([
            "Wie ist das Wetter heute?",
            "Was ist deine Lieblingsfarbe?",
            "Wie spät ist es?",
            "Erzähl mir einen Witz.",
            "Wie lautet dein Name?"
        ], start=1):
            expected_output += f"{index}. {question}\n"
        
        # Überprüfen der Ausgabe
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test für die Ausgabe von list_questions mit aktivem Debug-Modus
    def test_list_questions_with_debug(self):
        # Umleiten der Standardausgabe zu einem StringIO-Objekt für den Test
        captured_output = StringIO()
        sys.stdout = captured_output

        # Aufruf der Funktion mit aktivem Debug-Modus
        list_questions(debug=True)

        # Wiederherstellen der Standardausgabe
        sys.stdout = sys.__stdout__

        # Erwartete Ausgabe mit Debug-Modus
        expected_output = "Debug Mode aktiviert. Fragen werden angezeigt...\nFragen in der Wissensbasis:\n"
        for index, question in enumerate([
            "Wie ist das Wetter heute?",
            "Was ist deine Lieblingsfarbe?",
            "Wie spät ist es?",
            "Erzähl mir einen Witz.",
            "Wie lautet dein Name?"
        ], start=1):
            expected_output += f"{index}. {question}\n"
        
        # Überprüfen der Ausgabe
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    # Test-Runner starten
    unittest.main()
