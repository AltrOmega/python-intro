import unittest
from unittest.mock import patch
from my_awesome_lib.math_tools import bitEntropy, genericFloatBehaviour

class TestMathTools(unittest.TestCase):
    
    def test_bitEntropy_small_integers(self):
        """Test bitEntropy returning the original integer for integers < 8"""
        for i in range(8):
            self.assertEqual(bitEntropy(i), i, f"bitEntropy({i}) should return {i}")
    

    # Patching randint so it can be mocked later
    # Not gona place this comment on every test tho
    @patch('random.randint')
    def test_bitEntropy_no_bits_toggled(self, mock_randint):
        """Test bitEntropy when no bits are toggled (all random checks fail)"""
        # Set up the mock to return values that won't trigger bit toggling
        mock_randint.return_value = 11  # > 10% default chance
        
        original = 42  # 101010 in binary
        result = bitEntropy(original)
        
        # With no bits toggled, the result should be (original & ~7), which clears the lowest 3 bits
        expected = (original & ~7)  # 101000 in binary = 40

        self.assertEqual(result, expected)
    
    @patch('random.randint')
    def test_bitEntropy_all_bits_toggled(self, mock_randint):
        """Test bitEntropy when all bits are toggled (all random checks pass)"""
        # Set up the mock to return values that will trigger bit toggling
        mock_randint.return_value = 5  # <= 10% default chance
        
        original = 42  # 101010 in binary
        result = bitEntropy(original)
        
        # With all bits toggled, the result should be (original & ~7) | 7
        # This clears the lowest 3 bits and then sets them all to 1
        expected = (original & ~7) | 7  # 101111 in binary = 47
        self.assertEqual(result, expected)
    
    @patch('random.randint')
    def test_bitEntropy_specific_bits_toggled(self, mock_randint):
        """Test bitEntropy with specific bits toggled"""
        # Mock to toggle only the 1st and 3rd bits
        mock_randint.side_effect = [5, 15, 5]
        
        original = 42  # 101010 in binary
        result = bitEntropy(original)
        
        # This clears the lowest 3 bits and then sets bits 0 and 2
        expected = (original & ~7) | 5  # 101101 in binary = 45
        self.assertEqual(result, expected)
    
    @patch('random.randint')
    def test_bitEntropy_custom_chance(self, mock_randint):
        """Test bitEntropy with a custom chance percentage"""
        # Set up the mock to return values that will trigger bit toggling with 50% chance
        mock_randint.return_value = 30  # <= 50%
        
        original = 100  # 1100100 in binary
        result = bitEntropy(original, chancePerc=50)
        
        expected = (original & ~7) | 7  # 1100111 in binary = 103
        self.assertEqual(result, expected)
    
    def test_genericFloatBehaviour_returns_float(self):
        """Test that genericFloatBehaviour returns a float"""
        result = genericFloatBehaviour(3.14)
        self.assertIsInstance(result, float)
    
    def test_genericFloatBehaviour_changes_value(self):
        """Test that genericFloatBehaviour changes the input value"""
        original = 3.14
        result = genericFloatBehaviour(original)
        self.assertNotEqual(result, original)
    
    def test_genericFloatBehaviour_small_adjustment(self):
        """Test that genericFloatBehaviour makes only a small adjustment"""
        original = 3.14
        result = genericFloatBehaviour(original)

        # The adjustment should be very small
        self.assertAlmostEqual(result, original, places=12)
    
    @patch('random.randint')
    def test_genericFloatBehaviour_deterministic(self, mock_randint):
        """Test genericFloatBehaviour with deterministic random values"""
        # Set up the mock to return specific values
        mock_randint.side_effect = [2, 3]
        
        original = 5.0
        result = genericFloatBehaviour(original)
        
        # Checks if it has the expected decimal
        expected = original + 1/6 * 2 * 3 / 1_000_000_000_000_0
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
