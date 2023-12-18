import random
import sys

n = int(sys.argv[1])  # Size of the grid is 2n x 2n, but n is half the side length
m = int(sys.argv[2])  # Number of simulations to run
total_steps = 0  # Total number of steps for all simulations

# Run m simulations
for _ in range(m):
    # Initialize the walker's position at the center of the grid
    x, y = n, n
    steps = 0  # Steps taken in the current simulation

    # Run the simulation until the walker hits a boundary
    while 0 <= x < 2*n and 0 <= y < 2*n:
        direction = random.randint(1, 4)
        if direction == 1:  # North
            y += 1
        elif direction == 2:  # South
            y -= 1
        elif direction == 3:  # East
            x += 1
        elif direction == 4:  # West
            x -= 1
        
        steps += 1

        # Check if the walker has hit a boundary
        if x == 0 or x == 2*n - 1 or y == 0 or y == 2*n - 1:
            break

    total_steps += steps  # Add the steps taken in this simulation to the total

# Calculate the average number of steps
average_steps = total_steps / m

print(f'The average number of steps was: {average_steps}')
