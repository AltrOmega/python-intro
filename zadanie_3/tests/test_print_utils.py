import unittest
from unittest.mock import patch, MagicMock
import sys
import io
from my_awesome_lib.print_utils import chaosPrint, gibberishPrint, gibberishChaosPrint

class TestPrintUtils(unittest.TestCase):
    
    def setUp(self):
        # Redirect stdout to capture print output
        # You do this to capture prints output when it is used,
        # instead of puting it in standard out
        self.stdout_backup = sys.stdout
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output
    
    def tearDown(self):
        # Restore stdout so if other test ever use print 
        # things work as expected instead of beeing sent 
        # into the digital void.
        sys.stdout = self.stdout_backup
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    def test_chaosPrint_basic(self, mock_chaos):
        """Test that chaosPrint calls chaos with correct arguments and prints the result"""
        # Set up the mock to return a specific string
        mock_chaos.return_value = "chaotic text"
        
        # Call the function
        chaosPrint("Hello", "World")
        
        # Check that chaos was called with the correct arguments
        mock_chaos.assert_called_once_with("Hello World", 5)
        
        # Check that the output is correct
        self.assertEqual(self.captured_output.getvalue().strip(), "chaotic text")
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    def test_chaosPrint_custom_chance(self, mock_chaos):
        """Test chaosPrint with a custom chance percentage"""
        mock_chaos.return_value = "custom chaotic text"
        
        chaosPrint("Test", chancePerc=10)
        
        mock_chaos.assert_called_once_with("Test", 10)
        self.assertEqual(self.captured_output.getvalue().strip(), "custom chaotic text")
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    def test_chaosPrint_with_kwargs(self, mock_chaos):
        """Test chaosPrint with additional print kwargs"""
        mock_chaos.return_value = "end test"
        
        # Use end parameter to verify kwargs are passed to print
        chaosPrint("Test", end="!")
        
        mock_chaos.assert_called_once_with("Test", 5)
        self.assertEqual(self.captured_output.getvalue(), "end test!")
    
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishPrint_basic(self, mock_gibberish):
        """Test that gibberishPrint calls gibberish with correct arguments and prints the result"""
        mock_gibberish.return_value = "gibberish text"
        
        gibberishPrint("Hello", "World")
        
        mock_gibberish.assert_called_once_with("Hello World", 5)
        self.assertEqual(self.captured_output.getvalue().strip(), "gibberish text")
    
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishPrint_custom_chance(self, mock_gibberish):
        """Test gibberishPrint with a custom chance percentage"""
        mock_gibberish.return_value = "custom gibberish text"
        
        gibberishPrint("Test", chancePerc=10)
        
        mock_gibberish.assert_called_once_with("Test", 10)
        self.assertEqual(self.captured_output.getvalue().strip(), "custom gibberish text")
    
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishPrint_with_kwargs(self, mock_gibberish):
        """Test gibberishPrint with additional print kwargs"""
        mock_gibberish.return_value = "end test"
        
        gibberishPrint("Test", end="!")
        
        mock_gibberish.assert_called_once_with("Test", 5)
        self.assertEqual(self.captured_output.getvalue(), "end test!")
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishChaosPrint_basic(self, mock_gibberish, mock_chaos):
        """Test that gibberishChaosPrint calls both functions and prints the result"""
        mock_gibberish.return_value = "gibberish text"
        mock_chaos.return_value = "gibberish chaotic text"
        
        gibberishChaosPrint("Hello", "World")
        
        mock_gibberish.assert_called_once_with("Hello World", 5)
        mock_chaos.assert_called_once_with("gibberish text", 5)
        self.assertEqual(self.captured_output.getvalue().strip(), "gibberish chaotic text")
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishChaosPrint_custom_chance(self, mock_gibberish, mock_chaos):
        """Test gibberishChaosPrint with a custom chance percentage"""
        mock_gibberish.return_value = "gibberish text"
        mock_chaos.return_value = "custom gibberish chaotic text"
        
        gibberishChaosPrint("Test", chancePerc=10)
        
        mock_gibberish.assert_called_once_with("Test", 10)
        mock_chaos.assert_called_once_with("gibberish text", 10)
        self.assertEqual(self.captured_output.getvalue().strip(), "custom gibberish chaotic text")
    
    @patch('my_awesome_lib.print_utils.__tp.chaos')
    @patch('my_awesome_lib.print_utils.__tp.gibberish')
    def test_gibberishChaosPrint_with_kwargs(self, mock_gibberish, mock_chaos):
        """Test gibberishChaosPrint with additional print kwargs"""
        mock_gibberish.return_value = "gibberish text"
        mock_chaos.return_value = "end test"
        
        gibberishChaosPrint("Test", end="!")
        
        mock_gibberish.assert_called_once_with("Test", 5)
        mock_chaos.assert_called_once_with("gibberish text", 5)
        self.assertEqual(self.captured_output.getvalue(), "end test!")
    
    def test_chaosPrint_non_string_args(self):
        """Test chaosPrint with non-string arguments"""
        with patch('my_awesome_lib.print_utils.__tp.chaos') as mock_chaos:
            mock_chaos.return_value = "123 True"
            
            chaosPrint(123, True)
            
            # Check that the arguments were converted to strings and joined
            mock_chaos.assert_called_once_with("123 True", 5)
    
    def test_gibberishPrint_non_string_args(self):
        """Test gibberishPrint with non-string arguments"""
        with patch('my_awesome_lib.print_utils.__tp.gibberish') as mock_gibberish:
            mock_gibberish.return_value = "123 True"
            
            gibberishPrint(123, True)
            
            # Check that the arguments were converted to strings and joined
            mock_gibberish.assert_called_once_with("123 True", 5)
    
    def test_gibberishChaosPrint_non_string_args(self):
        """Test gibberishChaosPrint with non-string arguments"""
        with patch('my_awesome_lib.print_utils.__tp.gibberish') as mock_gibberish:
            with patch('my_awesome_lib.print_utils.__tp.chaos') as mock_chaos:
                mock_gibberish.return_value = "123 True"
                mock_chaos.return_value = "chaotic 123 True"
                
                gibberishChaosPrint(123, True)
                
                # Check that the arguments were converted to strings and joined
                mock_gibberish.assert_called_once_with("123 True", 5)
                mock_chaos.assert_called_once_with("123 True", 5)

if __name__ == '__main__':
    unittest.main()
