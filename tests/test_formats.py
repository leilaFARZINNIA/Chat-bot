from src.utils.formats import format_message
from datetime import datetime
import unittest

class TestFormatMessage(unittest.TestCase):
    def test_format_message(self):
        # Arrange
        sender = "Alice"
        message = "Hello, world!"
        
        # Act
        result = format_message(sender, message)
        
        # Extract the timestamp part and ensure it matches the expected format
        timestamp_str = result.split(' ')[0]
        
        # Assert
        self.assertTrue(datetime.strptime(timestamp_str, '%H:%M:%S'))  # Checks if timestamp is in HH:MM:SS format
        self.assertIn(sender, result)  # Check if sender name is in the result
        self.assertIn(message, result)  # Check if message is in the result

if __name__ == "__main__":
    unittest.main()