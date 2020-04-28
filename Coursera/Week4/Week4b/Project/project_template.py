# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [4, 4]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1,1]
    if direction == RIGHT:
        ball_vel= [random.randrange(120, 240)/60, random.randrange(-180, -60)/60]
    if direction == LEFT:
        ball_vel = [random.randrange(-240, -120)/60, random.randrange(60, 180)/60]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    # left gutter line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    # right gutter line
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        ball_vel[0] = - ball_vel[0]
        spawn_ball(RIGHT)
    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        spawn_ball(LEFT)
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[PAD_WIDTH - paddle1_pos , 0],[paddle1_pos, PAD_HEIGHT]], 8, "White")
    
    canvas.draw_polygon([[WIDTH - PAD_WIDTH + paddle2_pos, WIDTH],[WIDTH - PAD_WIDTH + paddle2_pos, HEIGHT - PAD_HEIGHT]], 8, "White")
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
