# Paddle Geometry and Control

## Three important constants in template

* HEIGHT - height of canvas
* PAD_HEIGHT - height of paddle
* PAD_WIDTH - width of paddle (and gutter)

## Two important variables (floats) per paddle

* left paddle:
  * paddle1_pos - vertical deistance of left paddle from top
  * paddle1_vel - vertical velocity of left paddle
* right paddle:
  * paddle2_pos - vertical deistance of right paddle from top
  * paddle2_vel - vertical velocity of right paddle

## Control scheme

* Continually update paddle1_pos/paddle2_pos in draw
* Modify paddle1_vel/paddle2_vel in keyup/keydown handlers
