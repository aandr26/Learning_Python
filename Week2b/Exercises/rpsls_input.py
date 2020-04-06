# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
    
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
    
    #
    # use if/elif/else to determine winner, print winner message
    #

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

     
    
# Handler for input field
def get_guess(guess):
    if (guess != "rock") or (guess != "Spock") or (guess != "paper") or (guess != "lizard") or (guess != "scissors"):
        rpsls(guess)
        print ("")
    else:
        print ("Error: Bad input " + '"'+ guess + '"' + " to rpsls.")



# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
