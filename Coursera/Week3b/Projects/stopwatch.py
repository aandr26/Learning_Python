# template for "Stopwatch: The Game"

# define global variables
import simplegui

WIDTH = 300
HEIGHT = 300
counter = 0
increment = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global counter
    global increment
    counter = counter
    increment = True
    timer.start()

def stop():
    global increment
    increment = False
    timer.stop()

def reset():
    global counter
    counter = 0
    tick()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    global increment
    if increment == True:
        start()
    elif increment == False:
        stop()
    counter += 1
    
# define draw handler
def draw(canvas):
    global counter
    canvas.draw_text(str(counter),[WIDTH/2, HEIGHT/2], 30, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", WIDTH, HEIGHT)


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(10, tick)
# start timer and frame
frame.start()
timer.start()

# Please remember to review the grading rubric