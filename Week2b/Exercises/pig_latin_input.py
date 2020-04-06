# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter == "a" or first_letter == "e" or
        first_letter == "i" or first_letter == "o" or
        first_letter == "u"):
        return (word + "way")
    else:
        return (rest_of_word + first_letter + "ay")

# Handler for input field
def get_input(txt):
    print (pig_latin(txt))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Enter your word", get_input, 100)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


