def is_even(number):
    """ Determines if the given parameter 'number' is odd or even """
    if (number % 2) == 0:
        return True
    elif (number % 2) != 0:
        return False
    else:
        return False

number = 3


even_number = is_even(number)

if even_number:
    print ("The number is even")
else:
    print ("The number is odd")

