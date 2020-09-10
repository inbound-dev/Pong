import pygame
import random
import sys


#NOTE
#when Drawing rectangles they use a screen then color then x,y,width,height

# ANY PART OF THE CODE THAT DOESNT WORK IS MARKED WITH **

#initalizes the screen and all running elements
pygame.init()

# Generates the clock
clock = pygame.time.Clock()

# Sets the FPS to 60

fps = clock.tick(60)

#set variables for colors
BLACK = 0,0,0
WHITE = 255,255,255
GREY = 25,25,25
#set variables for the screen component
Screen_Width = 1200
Screen_Height = 600

#variables for ganeration of the ball
Ball_Starting_Posx = (int(Screen_Width/2))
Ball_Starting_Posy = (int(Screen_Height/2))
Ball_Starting_Pos = Ball_Starting_Posx, Ball_Starting_Posy
Ball_Radius = 16

#sets the inital values of the movement of the ball
dx = 5
dy = 2

# changing the floats to ints
x = (int(Ball_Starting_Posx))
y = (int(Ball_Starting_Posy))

#variables for the generation of the scoreboard
Scoreboard_Width = Screen_Width
Scoreboard_Height = Screen_Height/16

#variables for the generation of the net
Net_Edge_Left = Screen_Width/2 - 8
Net_Width = 16
Net_height = Screen_Height

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Pong")

#fills the screen with the given color
screen.fill((BLACK))
pygame.display.flip()

#draws the net and the scoreboard

#Drawing the Scoreboard
pygame.draw.rect(screen, GREY, (0,0,Scoreboard_Width,Scoreboard_Height))
#Drawing the Net
pygame.draw.rect(screen, GREY, (Net_Edge_Left, 0, Net_Width, Net_height))

#drawing the ball for the start of the game
pygame.draw.circle(screen, WHITE, Ball_Starting_Pos, Ball_Radius)

#Draws the  net for the start of the game
pygame.draw.rect(screen, GREY, (Net_Edge_Left, 0, Net_Width, Net_height))

#Creates the paddles and sets the initial pos and directions

PaddleA_Starting_Posx = 16
PaddleA_Starting_Posy = Screen_Height/2 - 16

pygame.draw.rect(screen, WHITE, (PaddleA_Starting_Posx, PaddleA_Starting_Posy, 16, 96))

#main game loop
#exits the loop when the close button is hit
running = True
while running == True:

# Draws the borders of the screen every time the loop runs
    pygame.draw.rect(screen, BLACK, (Screen_Width - 16, Scoreboard_Height, 20, Screen_Height - Scoreboard_Height))
    pygame.draw.rect(screen, BLACK, (0, Screen_Height - 16, Screen_Width, 16))
    pygame.draw.rect(screen, BLACK, (0, Scoreboard_Height, 16, Screen_Height - Scoreboard_Height))

#Drawing the Scoreboard
    pygame.draw.rect(screen, GREY, (0,0,Scoreboard_Width,Scoreboard_Height))

# Draws a black box at the top of the screen under the scoreboard on bothsides of the net **

# Create the x and y directions for the ball
    x += dx
    y += dy

# Bounds Checking
    print(x,y, dx, dy)
# checking if the ball has hit the right side of the screen
    if x + dx > Screen_Width:
        dx =  -dx
# checking if the ball has hit the left of the screen
    if  x + dx <= 0:
        dx = -dx
# checking if the ball has hit the top of the screen **
    if y + dy < Scoreboard_Height:
        dy = dy + 4
# checking if the ball has hit the bottom of the screen
    if y + dx > Screen_Height:
        dy = -dy
# checking if the ball has hit the left paddle **

# checking if the ball has hit the right paddle **

# Drawing on the Ball on the screen

    #fill in the original Ball with black the redraw the net
    pygame.draw.circle(screen, BLACK, Ball_Starting_Pos, Ball_Radius)
    pygame.draw.rect(screen, GREY, (Net_Edge_Left, 0, Net_Width, Net_height))


#draw the new ball position the fill previous with screen color
    pygame.draw.circle(screen, BLACK, (x - dx,y - dy), Ball_Radius)
    pygame.draw.circle(screen, WHITE, (x, y), Ball_Radius)

    #Drawing the Scoreboard
    pygame.draw.rect(screen, GREY, (0,0,Scoreboard_Width,Scoreboard_Height))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
