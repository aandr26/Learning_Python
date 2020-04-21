# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"
counter = 0

# Timer handler
def tick():
    global frame
    global color
    if color == "Red":
        color = "Blue"
    elif color == "Blue":
        color = "Red"
    frame.set_canvas_background(color)
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)

tick()
# Start timer
frame.start()
timer.start()
