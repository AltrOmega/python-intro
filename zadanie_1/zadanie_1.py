import random

def generate_random_list(length, min, max):
    if length < 0:
        # https://docs.python.org/3/library/random.html#random.randint
        raise ValueError("Length must be a non-negative integer.")
    if min > max:
        # https://docs.python.org/3/library/random.html#random.randint
        raise ValueError("min_value must be less than or equal to max_value.")
    
    # https://docs.python.org/3/library/random.html#random.randint
    return [random.randint(min, max) for _ in range(length)]

if __name__ == '__main__':
    x = 0
    while x == 0:
        try:
            # https://docs.python.org/3/library/functions.html#int
            # https://docs.python.org/3/library/functions.html#input
            x = int(input("Gib max num to be rand generated, must be more than 0: "))
            list_1 = generate_random_list(5, 1, x)
            list_2 = generate_random_list(5, 1, x)
        except Exception as e:
            # https://docs.python.org/3/library/functions.html#print
            print("Wrong input with exception: ", e)
            print("Try again.")

    
    # https://docs.python.org/3/library/functions.html#print
    print(f"list_1: {list_1}")
    print(f"list_2: {list_2}")

    # https://docs.python.org/3/library/functions.html#zip
    jackpot = [a == b for a, b in zip(list_1, list_2)]
    if True in jackpot:
        # https://docs.python.org/3/library/functions.html#print
        print("Congratulations! You menaged to roll the same number on the same index in both lists.")