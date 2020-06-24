# implementation of card game - Memory

import simplegui
import random

carda = [0, 1, 2, 3, 4, 5 , 6, 7]
cardb = [0, 1, 2, 3, 4, 5 , 6, 7]
deck = carda + cardb
random.shuffle(deck)

exposed = []
# helper function to initialize globals
def new_game():
    global deck
    global exposed
    exposed = []
    random.shuffle(deck)
    print(deck)
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    selected = pos[0] // 50
    if selected not in exposed:
        exposed.append(selected)
    print(exposed)
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pointX = 10
    pointY = 70
    cardX = 0
    for card_index in range(len(deck)):
        if card_index in exposed:
            canvas.draw_text(str(deck[card_index]), (pointX, pointY), 60, 'White')
            canvas.draw_polygon([[cardX, 0], [cardX + 50, 0], [cardX + 50, 100], [cardX, 100]], 2, 'Red', 'Green')
            pointX += 50
        else:
            canvas.draw_polygon([[cardX, 0], [cardX + 50, 0], [cardX + 50, 100], [cardX, 100]], 2, 'Red', 'Green')
            cardX += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric