import pygame
import random

pygame.init()

# Function to draw paddles and ball
def draw_paddles_and_ball():
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(wn, BLUE, (dummy_ball_x, dummy_ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(second_left_paddle_x, second_left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(second_right_paddle_x, second_right_paddle_y, paddle_width, paddle_height))

# Function to handle keyboard input
def handle_keyboard_input(event):
    global right_paddle_vel, left_paddle_vel, second_right_paddle_vel, second_left_paddle_vel
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            right_paddle_vel = -0.9
        elif event.key == pygame.K_DOWN:
            right_paddle_vel = 0.9
        elif event.key == pygame.K_w:
            left_paddle_vel = -0.9
        elif event.key == pygame.K_s:
            left_paddle_vel = 0.9
        # Add other key handling logic here for gadgets or other features
        elif event.key == pygame.K_1:
            if left_gadget_remaining > 0:
                left_gadget = 1
        elif event.key == pygame.K_2:
            if right_gadget_remaining > 0:
                right_gadget = 1
        elif event.key == pygame.K_UP:
            second_right_paddle_vel = -0.9
        elif event.key == pygame.K_DOWN:
            second_right_paddle_vel = 0.9
        elif event.key == pygame.K_w:
            second_left_paddle_vel = -0.9
        elif event.key == pygame.K_s:
            second_left_paddle_vel = 0.9
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            right_paddle_vel = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            left_paddle_vel = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            second_right_paddle_vel = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            second_left_paddle_vel = 0


# Game Initialization
gadget_pair = 1
ch = int(input("Enter your choice for gadget pair: "))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2 

# Game Settings
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball Settings
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7
dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7

# Paddle Dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
second_left_paddle_y = second_right_paddle_y = HEIGHT/2 - paddle_height/2
second_left_paddle_x, second_right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0
second_right_paddle_vel = second_left_paddle_vel = 0

# Gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# Main Game Loop
while run:
    wn.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            handle_keyboard_input(event)

    # Ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
        dummy_ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        second_left_paddle_y = left_paddle_y
        second_right_paddle_y = right_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1 
        dummy_ball_vel_x *= -1

    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        second_right_paddle_y = right_paddle_y
        second_left_paddle_y = left_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4

    # Paddle's movement controls
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    if second_left_paddle_y >= HEIGHT - paddle_height:
        second_left_paddle_y = HEIGHT - paddle_height
    if second_left_paddle_y <= 0:
        second_left_paddle_y = 0
    if second_right_paddle_y >= HEIGHT - paddle_height:
        second_right_paddle_y = HEIGHT - paddle_height
    if second_right_paddle_y <= 0:
        second_right_paddle_y = 0

    # Paddle collisions
    # Left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_x = left_paddle_x + paddle_width
        ball_vel_x *= -1

    # Right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_x = right_paddle_x - radius
        ball_vel_x *= -1


    # Gadgets in action
    if left_gadget == 1:
        # Example gadget: Teleport left paddle to ball's y-position
        left_paddle_y = ball_y - paddle_height / 2
        left_gadget = 0
        left_gadget_remaining -= 1

    if right_gadget == 1:
        # Example gadget: Teleport right paddle to ball's y-position
        right_paddle_y = ball_y - paddle_height / 2
        right_gadget = 0
        right_gadget_remaining -= 1


    # Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    second_left_paddle_y += second_left_paddle_vel
    second_right_paddle_y += second_right_paddle_vel


    draw_paddles_and_ball()


    pygame.display.update()