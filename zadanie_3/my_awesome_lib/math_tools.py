import random

def bitEntropy(integer: int, chancePerc = 10):
    """
    Toggles up to 3 random low-order bits of the given integer based on a percentage chance.
    Works only on integers that have more than 3 bits aka x > 7.
    
    Args:
        integer (int): The input integer whose bits may be toggled.
        chancePerc (int, optional): The percentage chance for each bit to be toggled. Defaults to 10.
    
    Returns:
        int: The modified integer with potentially toggled bits.
    """
    num_bits = integer.bit_length()
    if num_bits <= 3:
        return integer
    
    effect_mask = 7
    chaos_mask = 0
    for i in [0, 1, 2]:
        if random.randint(1, 100) <= chancePerc:
            chaos_mask = chaos_mask | (1 << i)
    integer = (integer & ~effect_mask) | chaos_mask
    
    return integer

def genericFloatBehaviour(floating: float):
    """
    Modifies a floating-point number with a small random adjustment.
    
    Args:
        floating (float): The input floating-point number.
    
    Returns:
        float: The adjusted floating-point number.
    """
    floating += 1/6 * random.randint(1, 3) * random.randint(1, 3) / 1_000_000_000_000_0
    return floating

