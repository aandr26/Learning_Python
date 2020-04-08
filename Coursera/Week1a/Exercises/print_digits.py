import math

# Combine 
def print_digits(number):
    ones = number % 10
    tens = number // 10
    result = "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + ","
    print (result)
    return result

print_digits(42)
print_digits(99)
print_digits(5)

