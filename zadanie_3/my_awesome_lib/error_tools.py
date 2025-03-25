import random

def randomThrow(chancePerc: int = 1):
    """
    Raises a MemoryError with a given percentage chance.
    
    Args:
        chancePerc (int): The percentage chance to raise the error.
    """
    if random.randint(1, 100) <= chancePerc:
        raise MemoryError("System out of memory. All available RAM has been exhausted. Please close unused applications or increase system memory to continue.")

