import stddraw

stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

half_height = 0.5 / 2

center_x = 0.5
center_y = 0.5

triangle_height = (half_height * (3 ** 0.5)) / 2
top_vertex_y = center_y + triangle_height
bottom_left_vertex_x = center_x - half_height
bottom_right_vertex_x = center_x + half_height

stddraw.line(bottom_left_vertex_x, center_y - triangle_height, center_x, top_vertex_y)  # Left side
stddraw.line(center_x, top_vertex_y, bottom_right_vertex_x, center_y - triangle_height)  # Right side
stddraw.line(bottom_right_vertex_x, center_y - triangle_height, bottom_left_vertex_x, center_y - triangle_height)  # Base

stddraw.point(center_x, center_y)

stddraw.show()