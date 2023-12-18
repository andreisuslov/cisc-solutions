import stddraw
import math

stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

half_height = 0.5 / 2
center_x = 0.5
center_y = 0.5
triangle_height = (half_height * (math.sqrt(3) / 2))
dot_radius = 0.005
velocity = 0.005

y_coord = center_y - triangle_height

while True:
    stddraw.clear()
    
    stddraw.line(center_x - half_height, center_y - triangle_height, center_x + half_height, center_y - triangle_height)
    stddraw.line(center_x - half_height, center_y - triangle_height, center_x, center_y + triangle_height)
    stddraw.line(center_x, center_y + triangle_height, center_x + half_height, center_y - triangle_height)
    
    stddraw.filledCircle(center_x, y_coord, dot_radius)
    
    stddraw.show(10)
    
    y_coord += velocity
    
    slope = triangle_height / half_height
    left_boundary = center_x - (y_coord - (center_y - triangle_height)) / slope
    right_boundary = center_x + (y_coord - (center_y - triangle_height)) / slope
    
    if y_coord > center_y + triangle_height or y_coord < center_y - triangle_height:
        velocity = -velocity
    elif center_x < left_boundary or center_x > right_boundary:
        velocity = -velocity