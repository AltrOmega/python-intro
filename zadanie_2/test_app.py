import app as a
import unittest

# Normaly you'd like to have a separate test case for a given thing you are testing.
# Also those tests are not exaustive.
# Neiter of those things matter however, as this is a dummy task.
class TestApp(unittest.TestCase):
    def test_isOkEmailAddr(self):
        self.assertTrue(a.isOkEmailAddr("abc@def.com"))
        self.assertTrue(a.isOkEmailAddr("XYZ@XYZ.pl"))
        self.assertTrue(a.isOkEmailAddr("foo@bar.eu"))

        self.assertFalse(a.isOkEmailAddr("abc.com"))
        self.assertFalse(a.isOkEmailAddr("Xyz@@ballyn.com"))
        self.assertFalse(a.isOkEmailAddr("a@a.1"))
    
    def test_calcSquareArea(self):
        self.assertEqual(a.calcSquareArea(5), 25)
        self.assertEqual(a.calcSquareArea(0), 0)
        self.assertEqual(a.calcSquareArea(2.5), 6.25)
        self.assertAlmostEqual(a.calcSquareArea(1.1), 1.21)
        
    def test_filterOutValues(self):
        self.assertEqual(a.filterOutValues([1, 2, 3, 4, 5], [1, 3, 5]), [2, 4])
        self.assertEqual(a.filterOutValues([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(a.filterOutValues([1, 2, 3], [1], [2]), [3])
        self.assertEqual(a.filterOutValues([], [1, 2]), [])
        self.assertEqual(a.filterOutValues([1, 2, 3, 1, 2, 3], [1], [3]), [2, 2])
        
    def test_isPalindrome(self):
        self.assertTrue(a.isPalindrome("racecar"))
        self.assertTrue(a.isPalindrome("madam"))
        self.assertTrue(a.isPalindrome(""))
        self.assertTrue(a.isPalindrome("a"))
        
        self.assertFalse(a.isPalindrome("hello"))
        self.assertFalse(a.isPalindrome("world"))
        self.assertFalse(a.isPalindrome("abcde"))
        
    def test_isEven(self):
        self.assertTrue(a.isEven(2))
        self.assertTrue(a.isEven(0))
        self.assertTrue(a.isEven(-4))
        self.assertTrue(a.isEven(100))
        
        self.assertFalse(a.isEven(1))
        self.assertFalse(a.isEven(-3))
        self.assertFalse(a.isEven(99))

if __name__ == '__main__':
    unittest.main()