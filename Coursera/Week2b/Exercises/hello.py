
# Import the required modules
import simplegui

# Event handlers
def print_hello():
    """ This handler prints 'Hello' """
    print ("Hello")

def print_goodbye():
    """ This handler prints 'Goodbye' """
    print ("Goodbye")

def draw_handler(canvas):
    canvas.draw_text(print_goodbye, )

# Create the frame
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Hello", print_hello, 100)
frame.add_button("Goodbye", print_goodbye, 100)

# Start the event
frame.start()

