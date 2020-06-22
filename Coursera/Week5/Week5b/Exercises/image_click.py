# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
point = [WIDTH/2, HEIGHT/2]

# load test image
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')
image_size = [95, 93]
image_center = [image_size[0] / 2, image_size[1] /2]

# mouseclick handler
def click(pos):
    global point
    point = pos
    
    
# draw handler
def draw(canvas):
    canvas.draw_image(image, image_center, image_size, point, image_size)
    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# start frame
frame.start()