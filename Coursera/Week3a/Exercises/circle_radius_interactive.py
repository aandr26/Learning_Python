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
    ''' This function prints the circle to canvas, 
        and some text based on the value of ball radius '''
    global HEIGHT
    global WIDTH
    global ball_radius
    canvas.draw_circle([WIDTH/2, HEIGHT/2], ball_radius, 2, "Red")
    if ball_radius <= 5:
        canvas.draw_text("Cannot decrease size further", [WIDTH/4, (HEIGHT/2)+25], 20, "Blue")
    
# Event handlers for buttons
def increase_radius():
    ''' This function increases the radius of the circle '''
    global RADIUS_INCREMENT
    global ball_radius
    ball_radius += RADIUS_INCREMENT
    return ball_radius


def decrease_radius():
    ''' This function decreases the radius of the circle '''
    global RADIUS_INCREMENT
    global ball_radius
    # If that prevents the value of ball_radius from becoming negative.
    if ball_radius <= 5:
        ball_radius == 5
    else:
        ball_radius -= RADIUS_INCREMENT
    return ball_radius
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius, 100)
frame.add_button("Decrease radius", decrease_radius, 100)


# Start the frame animation
frame.start()