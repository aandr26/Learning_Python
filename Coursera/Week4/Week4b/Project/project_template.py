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
ball_vel = [1, 1]

paddle1_pos = 150
paddle2_pos = 150

paddle1_vel = 0
paddle2_vel = 0

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
    
    # collide and reflect off of left hand side of canvas
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        print (str(True) + "1L")
        if (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):
            print (str(True) + "2L")
            ball_vel[0] = - ball_vel[0]
        else:
            print (str(False) + "2L")
            spawn_ball(RIGHT)           
    else:
        print (str(False) + "1L and 2L")
        ball_pos[1] += ball_vel[1]
        ball_pos[0] += ball_vel[0]
        
    # collide and reflect off of right hand side of canvas
    if (ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS):
        print (str(True) + "1R")  
        if (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):     
            print (str(True) + "2R")
            ball_vel[0] = - ball_vel[0]
        else:
            print (str(False) + "2R")    
            spawn_ball(LEFT)
    else:
        print (str(False) + "1R and 2R")
        ball_pos[1] += ball_vel[1]
        ball_pos[0] += ball_vel[0]
            
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of bottom of canvas
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # keep paddle 1 - left paddle - on screen
    if paddle1_pos <= 1:
        paddle1_pos = 0
    if paddle1_pos >= (400 - PAD_HEIGHT):
        paddle1_pos = (400 - PAD_HEIGHT)
    
    # keep paddle 2 - right paddle - on screen
    if paddle2_pos <= 1:
        paddle2_pos = 0    
    if paddle2_pos >= (400 - PAD_HEIGHT):
        paddle2_pos = (400 - PAD_HEIGHT)
        
    # draw paddles
    
    # paddle 1 - left paddle
    canvas.draw_polygon([(PAD_WIDTH - PAD_WIDTH/2, paddle1_pos),(PAD_WIDTH/2, PAD_HEIGHT + paddle1_pos)], 8, "White")
    
    # paddle 2 - right paddle
    canvas.draw_polygon([(WIDTH - PAD_WIDTH + PAD_WIDTH/2, paddle2_pos),(WIDTH - PAD_WIDTH + PAD_WIDTH/2, PAD_HEIGHT + paddle2_pos)], 8, "White")
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # paddle 1 - left paddle
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 6
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 6
        
    # paddle 2 - right paddle
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 6
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 6
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
