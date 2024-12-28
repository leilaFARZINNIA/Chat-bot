from unittest.mock import patch, mock_open
import unittest
from io import StringIO
from src.args_parsing import list_questions

class TestListQuestions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="question,answer\nWhat is 2+2?,4\nWhat is the capital of France?,Paris")
    @patch("sys.stdout", new_callable=StringIO)  # Mocking the stdout to capture print output
    def test_list_questions(self, mock_stdout, mock_file):
        # Arrange
        file_name = "data/data.csv"

        # Act
        list_questions(file_name)

        # Assert
        expected_output = (
            "Fragen in der Wissensbasis:\n"
            "1. What is 2+2?\n"
            "2. What is the capital of France?\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        mock_file.assert_called_once_with(file_name, 'r')

if __name__ == "__main__":
    unittest.main()
