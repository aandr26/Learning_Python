# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print (color)

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

# Register event handlers
frame.add_button("Set Red", set_red, 100, 100)
frame.add_button("Set Blue", set_blue, 100, 100)
frame.add_button("Print", print_color, 100, 100) 

# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue
