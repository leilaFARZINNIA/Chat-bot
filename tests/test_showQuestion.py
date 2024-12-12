
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'chatbot')))


from chatbot.parse_args import list_questions


data_csv_mock = """Question,Answer
Was ist Python?,Eine Programmiersprache
Wie funktioniert eine Schleife?,Mit Iterationen
"""

class TestListQuestions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data=data_csv_mock)
    @patch("sys.stdout", new_callable=StringIO)
    def test_list_questions(self, mock_stdout, mock_file):
        """Testet die Funktion list_questions."""
   
        list_questions("mock_data.csv")
        
 
        expected_output = (
            "Fragen in der Wissensbasis:\n"
            "1. Was ist Python?\n"
            "2. Wie funktioniert eine Schleife?\n"
        )
        
       
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    unittest.main()