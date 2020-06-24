# This project is based on the article "Five mini programming projects for the Python beginner" found online
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# It is a simple dice game simulator
# The player roles the dice by clicking a button, 
# the dice result, the total number of rolls, 
# and the total value of all dice rolls are displayed.
# The player may start a new game play using the "New Game" button.

# Import the required module(s)
import simplegui
import random

# Initialize global variables
rolls = 0
result = 0
dice = 0
total = 0

# Define functions
def new_game():
    '''This function resets values to zero, effectively starting a new game.'''
    global rolls
    global total
    global dice
    rolls = 0
    total = 0
    dice = 0

def dice_roll():
    '''This function contains the basic game: 
    The number is generated, the guess tally is made, 
    and the total of all dice rolls is calculated.'''
    global rolls
    global total
    global dice
    dice = random.randint(1, 6)
    total += dice
    rolls += 1
    return dice
    

def draw_handler(canvas):
    '''This function draws the values from dice_roll onto the canvas.'''
    global dice
    global rolls
    global result
    canvas.draw_text(str(dice), (200, 200), 50, 'Red')
    # Dice coordinantes   (x1, y1)    (x2, y1)    (x2, y2)    (x1, y2)
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 'Red', 
    'White')
    if dice == 1:
        # One
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([200, 200], 7, 12, 'Black', 'Black')
    elif dice == 2:
        # Two
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([170, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 230], 7, 12, 'Black', 'Black')
    elif dice == 3:
        # Three
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([170, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([200, 200], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 230], 7, 12, 'Black', 'Black')
    elif dice == 4:
        # Four
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([170, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([170, 230], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 230], 7, 12, 'Black', 'Black')
    elif dice == 5:
        # Five
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([170, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([200, 200], 7, 12, 'Black', 'Black')
        canvas.draw_circle([170, 230], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 230], 7, 12, 'Black', 'Black')
    elif dice == 6: 
        # Six
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([170, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 170], 7, 12, 'Black', 'Black')
        canvas.draw_circle([170, 200], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 200], 7, 12, 'Black', 'Black')
        canvas.draw_circle([170, 230], 7, 12, 'Black', 'Black')
        canvas.draw_circle([230, 230], 7, 12, 'Black', 'Black')
    else:
        # One
        # Circle coordinantes (center_point, radius, line_width, line_color)
        canvas.draw_circle([200, 200], 7, 12, 'Black', 'Black')
    canvas.draw_text('Total rolls: '+ str(rolls), (15, 25), 20, 'White')
    canvas.draw_text('Total of dice: ' + str(total), (250, 25), 20, 'White')

# Define event handlers
frame = simplegui.create_frame("Roll the Dice", 400, 400)
roll_dice = frame.add_button("Roll the Dice", dice_roll, 50)
restart = frame.add_button("New Game", new_game, 50)
frame.set_draw_handler(draw_handler)

# Start frame and any timers
frame.start()