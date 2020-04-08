def print_digits(number):
    """ Calculates a number in the ones and tens position """
    ones = number % 10
    tens = number // 10
    if (number < 0) or (number >= 100):
        return "Error: Input is not a two-digit number."
    else:
        return "The tens digit is " + str(ones) + ", and the ones digit is " + str(tens) + "."
