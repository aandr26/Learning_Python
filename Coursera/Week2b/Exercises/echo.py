# Take an input and echo the input to the console

import simplegui

# Handlers
def get_input(inp):
    return inp

# Create the frame and register handlers

frame = simplegui.create_frame("Echo Chamber", 300, 300)
frame.add_input("Add your input", get_input, 100)

# Start the event
frame.start()