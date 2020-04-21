# Counter with buttons


import simplegui 

counter = 0
count = True
# Timer handler
def tick():
    global counter
    global count
    print (counter)
    if count == True:
        start()
        # Allows the program to resume at the count value 
        # when stop() was called and then increments from the value.
        counter += 1
    elif count == False:
        stop()
        
    
# Event handlers for buttons
def stop():
    ''' This function stops the timer but does not reset 
    the value of counter to 0 '''
    global counter
    global count
    count = False
    timer.stop()
    
def start():
    ''' This function restarts the timer after stop() has stopped the timer
    and continues incrementing the counter. '''
    global counter
    global count
    count = True
    # Perserves the current count
    counter = counter 
    timer.start()
    
def reset():
    ''' This function resets the value of counter to 0 '''
    global counter
    counter = 0
    tick()
    
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Stop", stop, 100)
frame.add_button("Start", start, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
