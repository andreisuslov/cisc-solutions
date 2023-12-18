import stddraw

# Constants for the game
WIDTH, HEIGHT = 1000, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 120
BALL_RADIUS = 15

# Initial positions
paddle_left_x = 100 - PADDLE_WIDTH / 2
paddle_right_x = WIDTH - (100 - PADDLE_WIDTH / 2)
paddle_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
ball_x = WIDTH / 2 - BALL_RADIUS
ball_y = HEIGHT / 2 - BALL_RADIUS

# Colors
BLUE = stddraw.BLUE
RED = stddraw.RED
BLACK = stddraw.BLACK
WHITE = stddraw.WHITE

# Function to draw paddles and ball
def draw_paddles_and_ball():
    # Draw left paddle
    stddraw.setPenColor(RED)
    stddraw.filledRectangle(paddle_left_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Draw right paddle
    stddraw.setPenColor(RED)
    stddraw.filledRectangle(paddle_right_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Draw ball
    stddraw.setPenColor(BLUE)
    stddraw.filledCircle(ball_x, ball_y, BALL_RADIUS)

# Main function containing the initial setup
def main():
    stddraw.setCanvasSize(WIDTH, HEIGHT)
    stddraw.setXscale(0, WIDTH)
    stddraw.setYscale(0, HEIGHT)

    while True:
        stddraw.clear(BLACK)
        draw_paddles_and_ball()
        stddraw.show()

# Ensuring the main function is called when the script is executed
if __name__ == '__main__':
    main()
