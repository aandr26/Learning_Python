# interactive application to convert a float into dollars and cents
import simplegui


# define global variables

value = 3.12

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string

# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [55, 110], 24, "White")

# define input handler
def input_handler(text):
    global value
    value = float(text)

# create a frame
frame = simplegui.create_frame("Convertor", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter value",input_handler, 100)

# start the frame
frame.start()