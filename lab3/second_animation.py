import stddraw

stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

side_length = 0.5
half_length = side_length / 2
velocity_horizontal = 0.005
velocity_diagonal = 0.005

x_horizontal = half_length
y_horizontal = half_length
x_diagonal = 1 - half_length
y_diagonal = 1 - half_length

while True:
    stddraw.clear()
    stddraw.square(half_length, half_length, half_length)
    stddraw.square(1 - half_length, 1 - half_length, half_length)
    stddraw.filledCircle(x_horizontal, y_horizontal, 0.005)
    stddraw.filledCircle(x_diagonal, y_diagonal, 0.005)
    stddraw.show(10)
    x_horizontal += velocity_horizontal
    x_diagonal += velocity_diagonal
    y_diagonal += velocity_diagonal
    
    if x_horizontal < 0 or x_horizontal > half_length * 2:
        velocity_horizontal = -velocity_horizontal
        x_horizontal += velocity_horizontal

    if x_diagonal < (1 - side_length) or x_diagonal > 1 or y_diagonal < (1 - side_length) or y_diagonal > 1:
        velocity_diagonal = -velocity_diagonal
        x_diagonal += velocity_diagonal
        y_diagonal += velocity_diagonal