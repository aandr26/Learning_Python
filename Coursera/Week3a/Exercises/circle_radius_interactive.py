# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    global HEIGHT
    global WIDTH 
    canvas.draw_circle([WIDTH/2, HEIGHT/2], ball_radius, 2, "Red")

# Event handlers for buttons
def increase_radius():
    global RADIUS_INCREMENT
    global ball_radius
    ball_radius += RADIUS_INCREMENT
    return ball_radius

def decrease_radius():
    global RADIUS_INCREMENT
    global ball_radius
    ball_radius -= RADIUS_INCREMENT
    return ball_radius
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius, 100)
frame.add_button("Decrease radius", decrease_radius, 100)


# Start the frame animation
frame.start()

