# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    global WIDTH
    radius += 2
    
    
# Draw handler
def draw(canvas):
    global WIDTH
    global HEIGHT
    global radius
    if radius <= (WIDTH/2):
        canvas.draw_circle([WIDTH/2, HEIGHT/2], radius, 2, "Red")
    elif radius >= (WIDTH/2):
        timer.stop()
        canvas.draw_circle([WIDTH/2, HEIGHT/2], radius, 2, "Red")
        canvas.draw_text("It's too big ya dingus!", [WIDTH/8, HEIGHT/2], 18 ,"Red")

# Create frame and timer
frame = simplegui.create_frame("Circle", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
timer.start()

