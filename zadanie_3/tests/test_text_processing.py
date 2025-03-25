import unittest
from unittest.mock import patch
from my_awesome_lib.text_processing import chaos, gibberish

class TestTextProcessing(unittest.TestCase):
    
    def test_chaos_empty_string(self):
        """Test if chaos returns an empty string when given an empty string"""
        self.assertEqual(chaos(""), "")
    
    def test_chaos_single_character(self):
        """Test that chaos returns the same character when given... a single character"""
        self.assertEqual(chaos("a"), "a")
    

    # Patching randint so it can be mocked later
    # Not gona place this comment on every test tho
    @patch('random.randint')
    def test_chaos_no_swaps(self, mock_randint):
        """Test chaos with no character swaps"""
        # Set up the mock to return values that won't trigger swaps
        mock_randint.side_effect = [101, 101, 101]  # All > 10*10 (default chance)
        
        original = "abc"
        result = chaos(original)
        self.assertEqual(result, original)
    
    @patch('random.randint')
    def test_chaos_with_swaps(self, mock_randint):
        """Test chaos with specific character swaps"""

        # swap with index 2 -> "cbad"
        # swap with index 0 -> "bcad"
        # no swap (150 > 100) -> "bcad"
        # swap with index 1 -> "bdac"
        mock_randint.side_effect = [50, 2, 50, 0, 150, 50, 1]
        
        result = chaos("abcd", chancePerc=10)
        self.assertEqual(result, "bdac")
    
    @patch('random.randint')
    def test_chaos_custom_chance(self, mock_randint):
        """Test chaos with a custom chance percentage"""
        # Set up the mock to return values that will trigger swaps with 5% chance
        mock_randint.side_effect = [45, 1, 60]  # First <= 5*10, second > 5*10
        
        result = chaos("ab", chancePerc=5)
        self.assertEqual(result, "ba")  # Only first character should be swapped
    
    def test_gibberish_empty_string(self):
        """Test that gibberish returns an empty string when given an empty string"""
        self.assertEqual(gibberish(""), "")
    
    @patch('random.randint')
    def test_gibberish_no_repeats(self, mock_randint):
        """Test gibberish when no character repeats occur"""
        # Set up the mock to return values that won't trigger repeats
        mock_randint.side_effect = [101, 101, 101]  # All > 10*10 (default chance)
        
        original = "abc"
        result = gibberish(original)
        self.assertEqual(result, original)
    
    @patch('random.randint')
    def test_gibberish_with_repeats(self, mock_randint):
        """Test gibberish with specific character repeats"""
        # repeat char 1: 2 times -> "aaa"
        # no repeat on char 2 (150 > 100) -> "aaab"
        # repeat char 3: 3 times -> "aaabcccc"
        mock_randint.side_effect = [50, 2, 150, 50, 3]
        
        result = gibberish("abc", chancePerc=10)
        self.assertEqual(result, "aaabcccc")
    
    @patch('random.randint')
    def test_gibberish_custom_chance(self, mock_randint):
        """Test gibberish with a custom chance percentage"""
        # Set up the mock to return values that will trigger repeats with 5% chance
        mock_randint.side_effect = [45, 1, 60]  # First <= 5*10, second > 5*10
        
        result = gibberish("ab", chancePerc=5)
        self.assertEqual(result, "aab")  # Only first character should be repeated
    
    @patch('random.randint')
    def test_gibberish_custom_max_repeats(self, mock_randint):
        """Test gibberish with a custom maximum number of repeats"""
        # Set up the mock to trigger repeats with max_repeats=5
        mock_randint.side_effect = [50, 5]
        
        result = gibberish("a", max_repeats=5)
        self.assertEqual(result, "aaaaaa")  # Original + 5 repeats
    
    @patch('random.randint')
    def test_gibberish_decimal_chance(self, mock_randint):
        """Test gibberish with a decimal chance percentage"""
        # Set up the mock to return values that will trigger repeats with 1.5% chance
        mock_randint.side_effect = [14, 2, 16]  # First <= 1.5*10, second > 1.5*10
        
        result = gibberish("ab", chancePerc=1.5)
        self.assertEqual(result, "aaab")  # Only first character should be repeated
    
    @patch('random.randint')
    def test_chaos_decimal_chance(self, mock_randint):
        """Test chaos with a decimal chance percentage"""
        # Set up the mock to return values that will trigger swaps with 1.5% chance
        mock_randint.side_effect = [14, 1, 16]  # First <= 1.5*10, second > 1.5*10
        
        result = chaos("ab", chancePerc=1.5)
        self.assertEqual(result, "ba")  # Characters should be swapped

if __name__ == '__main__':
    unittest.main()
