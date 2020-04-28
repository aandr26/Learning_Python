# Ball motion with an implicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
message = "Center"
color = "Red"
border = "Red"

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [3, 1] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    global color
    global border
    global message
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
        color = "Red"
        border = "Blue"
        message = "Left"
    # collide and reflect off of right hand side of canvas    
    if ball_pos[0] >=  WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
        color = "Blue"
        border = "Red"
        message = "Right"
    # collide and reflect off of top of canvas    
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
        color = "Green"
        border = "Yellow"
        message = "Top"
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]
        color = "Yellow"
        border = "Green"
        message = "Bottom"

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, border, color)
    # Draw message
    canvas.draw_text(message, [(WIDTH/2)-30, HEIGHT/2], 30, color)
    
# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
