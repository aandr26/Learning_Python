import simplegui

# Define draw handlers
def draw(canvas):
    canvas.draw_text("It works!", [100, 100], 24, "Red")

# Create frame
frame = simplegui.create_frame("Message", 300, 200)

# Register handlers
frame.set_draw_handler(draw)

# Start frame

frame.start()
