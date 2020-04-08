# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """ This function converts the value 'name' to a number """
    # convert name to number using if/elif/else
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    # if the value 'name' is not valid, return this error string
    else:
        return "Error: Name is not valid option"
    return name


def number_to_name(number):
    """ This function converts the value 'number' to a name """
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3 :
        number = "lizard"
    elif number == 4:
        number = "scissors"
    # if the value 'number' is not valid, return this error string
    else:
        return "Error: Number is not valid option"
    return number

    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games
    print (" ")
    # print out the message for the player's choice
    print ("Player chooses " + player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print ("Computer chooses " + comp_choice)
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message

    # These are the differences that result in the player winning
    if (difference == (-2)) or (difference == (-1)) or (difference == (3)) or (difference == (4)):
        print ("Player wins!")
    # These are the differences that result in the computer winning
    elif (difference == (-4)) or (difference == (-3)) or (difference == (1)) or (difference == (2)):
        print ("Computer wins!")
    # Conditions for a tie
    elif (difference == (0)):
        print ("Player and computer tie!")
    # Throw an error if bad values are used
    else:
        print ("Error: failed to resolve difference")
    return difference


# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric

