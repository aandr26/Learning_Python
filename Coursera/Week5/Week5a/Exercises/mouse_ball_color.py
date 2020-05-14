# Circle clicking problem

###################################################
# Student should enter code below

import simplegui
import math

# define global constants
RADIUS = 20
PURPLE_POS = [50, 40]
AQUA_POS = [150, 40]
LIME_POS = [250, 40]
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]
YELLOW_POS = [50, 160]
PINK_POS = [150, 160]
ORANGE_POS = [250, 160]
# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    if dist(pos, PURPLE_POS) < RADIUS:
        print("Purple")
    elif dist(pos,AQUA_POS) < RADIUS:
        print("Aqua")
    elif dist(pos, LIME_POS) < RADIUS:
        print("Lime")
    elif dist(pos, RED_POS) < RADIUS:
        print("Red")
    elif dist(pos, GREEN_POS) < RADIUS:
        print("Green")
    elif dist(pos, BLUE_POS) < RADIUS:
        print("Blue")
    elif dist(pos, YELLOW_POS) < RADIUS:
        print("Yellow")
    elif dist(pos, PINK_POS) < RADIUS:
        print("Pink")
    elif dist(pos, ORANGE_POS) < RADIUS:
        print("Orange")
          

# define draw
def draw(canvas):
    canvas.draw_circle(PURPLE_POS, RADIUS, 1, "Purple", "Purple")
    canvas.draw_circle(AQUA_POS, RADIUS, 1, "Aqua", "Aqua")
    canvas.draw_circle(LIME_POS, RADIUS, 1, "Lime", "Lime")
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    canvas.draw_circle(YELLOW_POS, RADIUS, 1, "Yellow", "Yellow")
    canvas.draw_circle(PINK_POS, RADIUS, 1, "Pink", "Pink")
    canvas.draw_circle(ORANGE_POS, RADIUS, 1, "Orange", "Orange")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


###################################################
# Sample output

#Clicked red ball
#Clicked green ball
#Clicked blue ball
#Clicked green ball
#Clicked red ball
#Clicked green ball
#Clicked blue ball
