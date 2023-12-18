import random
import sys

# Retrieve n from command line argument to define half the size of the box
n = int(sys.argv[1])  # The full grid is 2n x 2n

# Initialize walker's starting position at the center of the grid
x, y = n, n  # The center position when indexing from (0,0)

# Initialize step counter
c = 0

# Run the simulation until the walker hits a boundary
while 0 <= x < 2*n and 0 <= y < 2*n:
    step = random.randint(1, 4)
    if step == 1:  # North
        y += 1
    elif step == 2:  # South
        y -= 1
    elif step == 3:  # East
        x += 1
    elif step == 4:  # West
        x -= 1
    c += 1  # Increment step counter after each move

# Output the number of steps taken
print(f'The walker took {c} steps.')