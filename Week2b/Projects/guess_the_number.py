# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
#import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global total_guesses
    global num_range

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global total_guesses
    global remaining_guesses
    global range
    global num_range
    total_guesses = 7
    remaining_guesses = total_guesses
    range = "Range is [0,100)"
    secret_number = random.randrange(0,100)
    num_range = secret_number 
    print ("New game. " + str(range))
    print ("Number of remaining guesses is " + str(remaining_guesses))
    print ("")
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global total_guesses
    global remaining_guesses
    global range
    global num_range
    total_guesses = 10
    remaining_guesses = total_guesses
    range = "Range is [0,1000)"
    secret_number = random.randrange(0,1000)
    num_range = secret_number 
    print ("New game. " + str(range))
    print ("Number of remaining guesses is " + str(remaining_guesses))
    print ("")
    new_game()

def input_guess(guess):
    # main game logic goes here
    guess_out = int(guess)
    global remaining_guesses
    print ("Guess was " + str(guess_out))
    if remaining_guesses < 1: 
        remaining_guesses -= 1
        print ("Number of remaining guesses is " + str(remaining_guesses))
        print ("You ran out of guesses, the number was " + str(secret_number))
        print("")
        new_game()
    elif guess_out < secret_number:
        remaining_guesses -= 1
        print ("Number of remaining guesses is " + str(remaining_guesses))
        print ("Higher!")
        print("")
    elif guess_out > secret_number:
        remaining_guesses -= 1
        print ("Number of remaining guesses is " + str(remaining_guesses))
        print ("Lower!")
        print("")
    elif guess_out == secret_number:
        remaining_guesses -= 1
        print ("Number of remaining guesses is " + str(remaining_guesses))
        print ("Correct!")
        print("")
        new_game()
               
    
    
# create frame
#frame = simplegui.create_frame("What's my number?", 300, 300)
#
# register event handlers for control elements and start frame
#frame.add_input("Enter your guess", input_guess, 100)
#frame.add_button("Range is [0, 100)", range100, 100)
#frame.add_button("Range is [0, 1000)", range1000, 100)

new_game()
#frame.start()
# call new_game 



# always remember to check your completed program against the grading rubric 
range100()
secret_number = 74	
input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("73")
input_guess("74")
