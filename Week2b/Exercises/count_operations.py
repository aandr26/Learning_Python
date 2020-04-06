# GUI with buttons to manipulate global variable count
"""
Challenge: Given the program template below, implement four buttons that manipulate a global variable count as follows. 
The function reset() sets the value of count to be zero, the function increment() adds one to count, 
the function decrement() subtracts one from count, and the function print_count() prints the value of count to the console

"""
###################################################
# Student should enter their code below
import simplegui

# Define event handlers for four buttons
def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print (count)
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Count Operations", 300, 300)
frame.add_button("Reset", reset)
frame.add_butoon("Increment", increment)
frame.add_buton("Decrement", decrement)
frame.add_button("Print", print_count)

# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
