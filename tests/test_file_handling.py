from src.file_handling import load_questions_from_csv, validate_file_path
from unittest.mock import mock_open, patch
import unittest
import os

class TestLoadQuestionsFromCsv(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data=(
        "question,choice1,choice2,choice3,choice4,correct_answer\n"
        "What is 2+2?,1,2,3,4,4\n"
        "What is the capital of France?,Berlin,Madrid,Paris,Rome,Paris\n"
    ))
    def test_load_questions_from_csv(self, mock_file):
        # Expected result
        expected = [
            {
                'question': 'What is 2+2?',
                'choices': ['1', '2', '3', '4'],
                'correct_answer': '4'
            },
            {
                'question': 'What is the capital of France?',
                'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
                'correct_answer': 'Paris'
            }
        ]
        
        # Call the function
        result = load_questions_from_csv("dummy.csv")
        
        # Assertions
        self.assertEqual(result, expected)
        mock_file.assert_called_once_with("dummy.csv", 'r')
      
if __name__ == "__main__":
    unittest.main()