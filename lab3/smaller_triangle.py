import stddraw 

# Set the canvas size and scale to operate in a unit square
stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)


stddraw.line(0.25, 0, 0.5, 0.5)   # Left side
stddraw.line(0.5, 0.5, 0.75, 0)   # Right side
stddraw.line(0.75, 0, 0.25, 0)    # Base

# For the smaller triangle, the center is at (0.5, 1/3 * height)
stddraw.point(0.5, 1/6)

stddraw.show()