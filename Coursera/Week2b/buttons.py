# calculator with all buttons


import simplegui


# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print ("Store = ", store)
    print ("Operand = ", operand)
    print ("")
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()

def add():
    """ add operand to store """
    global store, operand
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store, operand
    store = store - operand
    output()

def multi():
    """ multiply store by operand """
    global store, operand
    store = store * operand
    output()

def div():
    """ divide store by operand """
    global store, operand
    store = store / operand
    output()

def enter(inp):
    global operand
    operand = int(inp)
    output()

# Create frame
frame = simplegui.create_frame("Calculator", 300, 300)

# Register even handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Multiply", multi, 100)
frame.add_button("Divide", div, 100)
frame.add_input("Enter operand", enter, 100)

# Start
frame.start()
