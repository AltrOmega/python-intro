import unittest
from unittest.mock import patch
from my_awesome_lib.error_tools import randomThrow

class TestErrorTools(unittest.TestCase):
    
    # Patching randint so it can be mocked later
    # Not gona place this comment on every test tho
    @patch('random.randint')
    def test_randomThrow_when_below_threshold(self, mock_randint):
        """Test that randomThrow raises MemoryError when random value is below or equal to threshold"""
        # Set up the mock to return a value that will trigger the error
        mock_randint.return_value = 1  # equals default trigger %
        
        with self.assertRaises(MemoryError) as context:
            randomThrow()
        
        self.assertIn("System out of memory", str(context.exception))
        
        mock_randint.assert_called_once_with(1, 100)
    
    @patch('random.randint')
    def test_randomThrow_when_above_threshold(self, mock_randint):
        """Test that randomThrow doesn't raise MemoryError when random value is above threshold"""
        # Same as before. Set up the mock to return a value that won't trigger the error
        mock_randint.return_value = 2  # is > than default %
        
        # Should never throw here since (1 <= 2) == False
        try:
            randomThrow()
        except MemoryError:
            self.fail("randomThrow() raised MemoryError unexpectedly!")
    
    @patch('random.randint')
    def test_randomThrow_with_custom_chance(self, mock_randint):
        """Test randomThrow with a custom chance percentage"""
        # Again .Set up the mock to return a value that will trigger the error with 50% chance
        mock_randint.return_value = 25  # This is <= 50%
        
        # 25 <= 50 -> will always throw
        with self.assertRaises(MemoryError):
            randomThrow(chancePerc=50)
        
        mock_randint.assert_called_once_with(1, 100)
    
    @patch('random.randint')
    def test_randomThrow_with_zero_chance(self, mock_randint):
        """Test randomThrow with 0% chance should never throw"""
        # Set up the mock to return the default 1%
        mock_randint.return_value = 1
        
        # With 0% chance, it will never throw
        try:
            randomThrow(chancePerc=0)
        except MemoryError:
            self.fail("randomThrow(chancePerc=0) raised MemoryError unexpectedly!")
    
    @patch('random.randint')
    def test_randomThrow_with_hundred_percent_chance(self, mock_randint):
        """Test randomThrow with 100% chance should always throw"""
        # Self explanatory at this point i think
        mock_randint.return_value = 100
        
        # 100% chance will always throw
        with self.assertRaises(MemoryError):
            randomThrow(chancePerc=100)

if __name__ == '__main__':
    unittest.main()
