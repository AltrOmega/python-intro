from . import text_processing as __tp
# This import throws when this script is run
# so i guess dont put a __name__ == __main__ here in the future

# since the funcions here are ment to override print you have to have
# a refrence to the original print to... print y know
# i tried using __builtins__.print but it... works only here and not in unittests for some reason
print_origin = print

def chaosPrint(*args, chancePerc=5, **kwargs):
    """
    Prints a string with random character swaps based on a percentage chance.
    Ment to override default print.
    
    Args:
        *args: Positional arguments to be printed.
        chancePerc (int, optional): The percentage chance for character swaps. Defaults to 5.
        **kwargs: Additional keyword arguments for the print function.
    """
    original_string = ' '.join(map(str, args))
    chaotic_string = __tp.chaos(original_string, chancePerc)
    print_origin(chaotic_string, **kwargs)


def gibberishPrint(*args, chancePerc=5, **kwargs):
    """
    Prints a string with random character repetitions based on a percentage chance.
    
    Args:
        *args: Positional arguments to be printed.
        chancePerc (int, optional): The percentage chance for character repetitions. Defaults to 5.
        **kwargs: Additional keyword arguments for the print function.
    """
    original_string = ' '.join(map(str, args))
    chaotic_string = __tp.gibberish(original_string, chancePerc)
    print_origin(chaotic_string, **kwargs)


def gibberishChaosPrint(*args, chancePerc=5, **kwargs):
    """
    Prints a string with both random character swaps and repetitions.
    
    Args:
        *args: Positional arguments to be printed.
        chancePerc (int, optional): The percentage chance for both swaps and repetitions. Defaults to 5.
        **kwargs: Additional keyword arguments for the print function.
    """
    original_string = ' '.join(map(str, args))
    chaotic_string = __tp.gibberish(original_string, chancePerc)
    chaotic_string = __tp.chaos(chaotic_string, chancePerc)
    print_origin(chaotic_string, **kwargs)
