from src.file_handling import load_questions_from_csv
from unittest.mock import mock_open, patch
import unittest


class TestLoadQuestionsFromCSV(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="question,choice1,choice2,choice3,choice4,correct_answer\nWhat is 2+2?,4,3,5,6,4\nWhat is the capital of France?,Paris,London,Berlin,Madrid,Paris")
    def test_load_questions_from_csv(self, mock_file):
        # Arrange
        expected_output = [
            {
                'question': 'What is 2+2?',
                'choices': ['4', '3', '5', '6'],
                'correct_answer': '4'
            },
            {
                'question': 'What is the capital of France?',
                'choices': ['Paris', 'London', 'Berlin', 'Madrid'],
                'correct_answer': 'Paris'
            }
        ]

        # Act
        result = load_questions_from_csv("fake_file.csv")
        
        # Assert
        self.assertEqual(result, expected_output)
        mock_file.assert_called_once_with("fake_file.csv", 'r')

if __name__ == "__main__":
    unittest.main()