# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.

def reset():
    """ This function resets the global variable count to zero"""
    global count
    count = 0

def increment():
    """ This function increases the value of count by one"""
    global count
    count += 1

def decrement():
    """ This function decreases the value of count by one"""
    global count
    count -= 1

def print_count():
    """ This function prints the value of count to the console"""
    global count
    print (count)
    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()


####################################################
# Output
#1
#2
#-2