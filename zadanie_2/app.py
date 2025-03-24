from typing import List



def isOkEmailAddr(email: str) -> bool:
    '''
    Validates if a string is a proper email address.
    Valid emails have a single @ symbol and end with a valid domain extension.
    ''' # Yes i know there are more requirements to have a fully valid email, i chose to ignore them.
    if email.count('@') != 1:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
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
    return sideLength * sideLength



# Honestly, I am kind of confused why I used the * operator here,
# but I am not rewriting the unit tests to change this, so here
# it stands... unchanged... unyielding...
def filterOutValues(source: list, *filters: list) -> list:
    """
    Filters out values from the source list that appear in any of the filter lists.
    Returns a new list with the remaining values.
    """
    filter = []
    [filter.extend(filter_) for filter_ in filters] # list comprehension abuse for the win
    return [item for item in source.copy() if item not in filter]



def isPalindrome(string: str) -> bool:
    '''
    Checks if a string is a palindrome (reads the same forward and backward).
    Empty strings and single characters are considered palindromes.
    '''
    return string == string[::-1]



def isEven(integer: int) -> bool:
    '''
    Checks if an integer is even.
    '''
    return integer % 2 == 0
