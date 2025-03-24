from typing import List



def isOkEmailAddr(email: str) -> bool:
    '''
    Validates if a string is a proper email address.
    Valid emails have a single @ symbol and end with a valid domain extension.
    ''' # Yes i know there are more requirements to have a fully valid email, i chose to ignore them.
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    
    if email.count('@') != 1:
        return False

    # This will always split in two since there
    # has to be a single @ somewhere in the email by this point
    username, domain = email.split('@') 
    if not username or not domain:
        return False
    
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    
    extension = domain_parts[-1]
    if len(extension) < 2 or not extension.isalpha():
        return False
    
    return True



def calcSquareArea(sideLength: float) -> float:
    '''
    Calculates the area of a square given its side length.
    '''
    if not isinstance(sideLength, (int, float)):
        raise TypeError("Side length must be a number")
    
    if sideLength < 0:
        raise ValueError("Side length cannot be negative")
    
    return sideLength * sideLength



# Honestly, I am kind of confused why I used the * operator here,
# but I am not rewriting the unit tests to change this, so here
# it stands... unchanged... unyielding...
def filterOutValues(source: list, *filters: list) -> list:
    """
    Filters out values from the source list that appear in any of the filter lists.
    Returns a new list with the remaining values.
    """
    if not isinstance(source, list):
        raise TypeError("Source must be a list")
    
    filter = []
    [filter.extend(filter_) for filter_ in filters] # list comprehension abuse for the win
    return [item for item in source.copy() if item not in filter]



def isPalindrome(string: str) -> bool:
    '''
    Checks if a string is a palindrome (reads the same forward and backward).
    Empty strings and single characters are considered palindromes.
    '''
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    return string == string[::-1]



def isEven(integer: int) -> bool:
    '''
    Checks if an integer is even.
    '''
    if not isinstance(integer, int):
        raise TypeError("Input must be an integer")
    
    return integer % 2 == 0
