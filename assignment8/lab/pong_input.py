import stddraw
import stdio
import math
import random



#---------------------------------------------------
# CONTROLS - 
# "W" for up and "S" for down as Player 1
# "I" for up and "K" for down as Player 2
#---------------------------------------------------




Player1DefaultYCoord = 40
Player2DefaultYCoord = 40

Paddle_Movement_1 = 0
Paddle_Movement_2 = 0

DefaultBallCoordX = 50
DefaultBallCoordY = 50

#These randrange generators randomly create the X and Y Velocities of the ball

VelocityXRandom = random.randrange(-16, 16)
VelocityYRandom = random.randrange(-16, 16)

#Diving the number allows for more angle possibilities while still having the ball
#move an a manageable speed at a decent framerate

VelocityX = VelocityXRandom / 13
VelocityY = VelocityYRandom / 13

if VelocityX > 1 or VelocityY > 2:
    VelocityX = VelocityX / 2
    VelocityY = VelocityY / 2




def paddle_creation(a):
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
    global DefaultBallCoordX
    global DefaultBallCoordY
    global VelocityX
    global VelocityY

    if DefaultBallCoordY <= 0 or DefaultBallCoordY >= 100:
        VelocityY = VelocityY * -1

    stddraw.point(DefaultBallCoordX, DefaultBallCoordY)
    DefaultBallCoordX = DefaultBallCoordX + VelocityX
    DefaultBallCoordY = DefaultBallCoordY + VelocityY

    



def window_creation():
    stddraw.setCanvasSize(800, 800)
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)

def collision_detection():
    pass

def main():
    window_creation()
    while True:
        stddraw.clear()
        KeyDetected = key_detection()
        paddle_creation(KeyDetected)
        ball_creation()
        collision_detection()
        stddraw.show(20)

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


