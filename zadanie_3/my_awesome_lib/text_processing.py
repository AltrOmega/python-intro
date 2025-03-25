import random

def chaos(string: str, chancePerc = 10):
    """
    Randomly swaps characters in a string based on a percentage chance.
    
    Args:
        string (str): The input string.
        chancePerc (float, optional): The percentage chance for character swaps. 
            Can include tenths (e.g., 1.1 for 1.1%). If more than one decimal 
            place is provided (e.g., 2.12), it will be rounded to one decimal 
            place. Defaults to 10.
    
    Returns:
        str: The modified string with swapped characters.
    """
    chars = list(string)
    
    for i in range(len(chars)):
        if random.randint(1, 1000) <= chancePerc* 10:
            swap_pos = random.randint(0, len(chars) - 1)
            chars[i], chars[swap_pos] = chars[swap_pos], chars[i]
    
    return ''.join(chars)

def gibberish(string: str, chancePerc = 10, max_repeats = 3):
    """
    Randomly repeats characters in a string based on a percentage chance.
    
    Args:
        string (str): The input string.
        chancePerc (float, optional): The percentage chance for character repeats. 
            Can include tenths (e.g., 1.1 for 1.1%). If more than one decimal 
            place is provided (e.g., 2.12), it will be rounded to one decimal 
            place. Defaults to 10.
        max_repeats (int, optional): The maximum number of repetitions for a character. Defaults to 3.
    
    Returns:
        str: The modified string with repeated characters.
    """
    result = []
    
    for char in string:
        result.append(char)
        
        if random.randint(1, 1000) <= chancePerc * 10:
            repeats = random.randint(1, max_repeats)
            result.extend([char] * repeats)
    
    return ''.join(result)
