# Info

**Program Structure:**

    1. Globals (state)
    2. Helper functions
    3. Classes
    4. Define event handlers
    5. Create a frame
    6. Register event handlers
    7. Start frame & timers

```python

# This is how you make a multi line string
# This is a comment

```

**Event-driven drawing:**

* Computer monitor - 2D grid of pixels stored in frame buffer.
* Computers update the monitor based on the frame buffer at rate of around 60-72 times a second - refresh rate.
* Many applications will register a special function called a "draw handler".

**CodeSkulptor:**

1. Register the draw handler using a simpleGUI commands.
2. Call the draw handler at around 60 times per second.
3. Draw handler updates the canvas using a collection of draw commands that include draw_text, draw_line, draw_circle.
