# Ball grid solution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS

ball_list = [1,2,3,4,5,6,7,8,9,10]

# define draw
def draw(canvas):
    for ball in ball_list:
        y = 40
        canvas.draw_circle([40, y], BALL_RADIUS, 1, "Purple", "Purple")
        y += 40
        for ball in ball_list:
            x = 40
            canvas.draw_circle([40, y], BALL_RADIUS, 1, "Purple", "Purple")
            x += 40
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

