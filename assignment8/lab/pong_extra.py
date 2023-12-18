import stddraw
import stdio
import math
import random

# This Program is the final Pong program that breaks whenever someone wins (followed
# by a victory message), This also prints key information to the terminal for debugging

#---------------------------------------------------
# CONTROLS - 
# "W" for up and "S" for down as Player 1
# "I" for up and "K" for down as Player 2
#---------------------------------------------------


#Global Variables that we will be using for movements, These are for the 
#default settings when you start the game

#Default Player Coords are the Default Y Coords for both Rectangles
#Paddle Movements start at 0 because they are mutable variables
#that get added or subtracted to the default starting position
#Which makes the rectnagles move



Player1DefaultYCoord = 40
Player2DefaultYCoord = 40

Paddle_Movement_1 = 0
Paddle_Movement_2 = 0

DefaultBallCoordX = 50
DefaultBallCoordY = 50

p1_pdl_y = 0
p2_pdl_y = 0

#These randrange generators randomly create the X and Y Velocities of the ball

VelocityXRandom = random.randrange(-16, 16)
VelocityYRandom = random.randrange(-16, 16)

#Diving the number allows for more angle possibilities while still having the ball
#move an a manageable speed at a decent framerate. 

VelocityX = VelocityXRandom / 14
VelocityY = VelocityYRandom / 14

if VelocityX < 5 or VelocityY < 5:
    VelocityX = VelocityX * 1.2
    VelocityY = VelocityY * 1.2

if VelocityX > 7 or VelocityY > 7:
    VelocityX = VelocityX / 2
    VelocityY = VelocityY / 2


# paddle_creation is where the paddle get created in each frame

def paddle_creation(a):
    global p1_pdl_y
    global p2_pdl_y 
    global Player1DefaultYCoord
    global Player2DefaultYCoord
    global Paddle_Movement_1
    global Paddle_Movement_2

    #a = the y Coords

    #the coordinates are for the bottom left hand corner
    #this is the starting position of the first rectangle
    



    if a == 'w':
        Paddle_Movement_1 += 5

    if a == 's':
        Paddle_Movement_1 -= 5

    if a == 'i':
        Paddle_Movement_2 += 5

    if a == 'k':
        Paddle_Movement_2 -= 5

    if a == 0:
        Paddle_Movement_1 += 0
        Paddle_Movement_1 += 0

    p1_pdl_x = 10
    p1_pdl_y = Player1DefaultYCoord + Paddle_Movement_1
    p1_pdl_w = 3
    p1_pdl_h = 20

    stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
    
    # to get the x coordinate for the 2nd paddle, I had to subract 13 from 100
    #10 so that I am equally far away from the edge as p1, and the extra 3 for the width
    #of the rectangle
    
    #this is the starting position of the second rectangle

    p2_pdl_x = 87
    p2_pdl_y = Player2DefaultYCoord + Paddle_Movement_2
    p2_pdl_w = 3
    p2_pdl_h = 20

    stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)

    
def key_detection():
    # Function prints out keyboard player movement info to terminal for debugging
    if stddraw.hasNextKeyTyped():
        CurrentKey = stddraw.nextKeyTyped()
        if CurrentKey == 'w':
            print ("p1 up")
            return 'w'
        if CurrentKey == 's':
            print ("p1 down")
            return 's'
        if CurrentKey == 'i':
            print ("p2 up")
            return 'i'
        if CurrentKey == 'k':
            print ("p2 down")
            return 'k'
    else:
        return 0
    


def ball_creation():

    global p1_pdl_y
    global p2_pdl_y 

    global Player1DefaultYCoord
    global Player2DefaultYCoord

    global DefaultBallCoordX
    global DefaultBallCoordY

    global VelocityX
    global VelocityY

    # This if statements detects if the ball hit the top or bottom boundaries, and makes the ball bounce

    if DefaultBallCoordY <= 0 or DefaultBallCoordY >= 100:
        VelocityY = VelocityY * -1

    # Draw the ball in the next frame

    stddraw.point(DefaultBallCoordX, DefaultBallCoordY)

    # Calculates the next ball location with the randomized velocity

    DefaultBallCoordX = DefaultBallCoordX + VelocityX
    DefaultBallCoordY = DefaultBallCoordY + VelocityY

    # This is the Y value of the bottom left point of the rectangles, if you add 20, you get the top portion.
    # The importance of this is that you then have the y values where the ball could be hitting the paddle.

    Player1BottomCollisionDetectorY = p1_pdl_y
    Player2BottomCollisionDetectorY = p2_pdl_y

    Player1TopCollisionDetectorY = p1_pdl_y + 20
    Player2TopCollisionDetectorY = p2_pdl_y + 20

    # This Calculates the X values in which the ball could be hitting the paddle. 
    # 10 and 87 are the amount of units away from the border of the window that
    # each bottom left corner X Coord value is away (in units). So you have to add
    # 3 to account for the width of the rectangles.

    Player1LeftCollisionDetectorX = 10
    Player1RightCollisionDetectorX = 10 + 3
    
    Player2LeftCollisionDetectorX = 87
    Player2RightCollisionDetectorX = 87 + 3

    # These if statements are what detects if the ball has hit a paddle of not

    if (Player1BottomCollisionDetectorY <= DefaultBallCoordY <= Player1TopCollisionDetectorY) and (Player1LeftCollisionDetectorX <= DefaultBallCoordX <= Player1RightCollisionDetectorX):
        VelocityX = VelocityX * -1

    if (Player2BottomCollisionDetectorY <= DefaultBallCoordY <= Player2TopCollisionDetectorY) and (Player2LeftCollisionDetectorX <= DefaultBallCoordX <= Player2RightCollisionDetectorX):
        VelocityX = VelocityX * -1





def window_creation():
    # Set the window size and unit scaling
    stddraw.setCanvasSize(800, 800)
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)


def main():
    window_creation()
    while True:
        stddraw.clear()
        KeyDetected = key_detection()
        paddle_creation(KeyDetected)
        ball_creation()
        stddraw.show(38)

        if DefaultBallCoordX <= 0:
            stdio.writeln("-------------")
            stdio.writeln("  GAME OVER  ")
            stdio.writeln("Player 2 Won!")
            stdio.writeln("-------------")
            break
        if DefaultBallCoordX >= 100:
            stdio.writeln("-------------")
            stdio.writeln("  GAME OVER  ")
            stdio.writeln("Player 1 Won!")
            stdio.writeln("-------------")
            break
            
        

if __name__ == '__main__':
    main()


