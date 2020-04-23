# template for "Stopwatch: The Game"

# define global variables
import simplegui

WIDTH = 300
HEIGHT = 300
SCORE = 30
counter = 0
increment = False
click = False
total_guesses = 0
correct_guesses = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ''' A = minutes, B = tens of seconds, C = seconds > tens of seconds
    D = remaining tens of seconds.  
    A:BC:D '''
    A = ((t // 10) // 60)
    #print ("This is A " + str(A))
    B = (((t // 10) % 60) // 10)
    #print ("This is B " + str(B))
    C = (((t // 10) % 60) % 10)
    #print ("This is C " + str(C))
    D = ((t // 1) % 60) % 10
    #print ("This is D " + str(D))
    return (str(A) + ":" + str(B) + str(C)+ "." + str(D))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    ''' Starts the game '''
    global counter
    global increment
    global click
    counter = counter
    increment = True
    click = True
    timer.start()

def stop():
    ''' Stops the timer, and increments the total_guesses by 1. 
    If timer is stopped on an even second, 
    correct_guesses is also incremented by 1
    '''
    global counter
    global increment
    global click
    global total_guesses
    global correct_guesses
    increment = False
    timer.stop()
    if click:
        click = False
        # Prevents total_guesses from incrementing if timer is not running.
        if not increment:
            total_guesses += 1
    if (counter > 0) and ((counter % 10) == 0):
        correct_guesses += 1
    

def reset():
    ''' Resets all counters in the game. '''
    global counter
    global correct_guesses
    global total_guesses
    counter = 0
    correct_guesses = 0
    total_guesses = 0
    tick()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    global increment
    if increment == True:
        start()
        counter += 1
    elif increment == False:
        stop()
    
    
# define draw handler
def draw(canvas):
    global counter
    canvas.draw_text(str(format(counter)),[WIDTH/2.5, HEIGHT/2], 30, "Red")
    canvas.draw_text(str(correct_guesses) + "/" + str(total_guesses), [260-SCORE, 30], SCORE, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", WIDTH, HEIGHT)


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
# start timer and frame
frame.start()
timer.start()

# Please remember to review the grading rubric