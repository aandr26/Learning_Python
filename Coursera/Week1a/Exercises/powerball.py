import random
# Powerball
def powerball():
    number1 = random.randrange(1,60)
    number2 = random.randrange(1,60)
    number3 = random.randrange(1,60)
    number4 = random.randrange(1,60)
    number5 = random.randrange(1,60)
    winning = number1 = random.randrange(1,36)
    output = "Today's numbers are " + str(number1) + ", " + str(number2) + ", " + str(number3) + ", " + str(number4) + " and " + str(number5) + ". The Powerball number is " + str(winning) + "."
    print (output)
powerball()