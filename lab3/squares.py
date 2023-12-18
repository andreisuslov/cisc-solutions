import stddraw

stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

side_length = 0.5
half_length = side_length / 2

stddraw.square(0.5 + half_length, 0.5 + half_length, half_length)
stddraw.filledCircle(0.5 + half_length, 0.5 + half_length, 0.005)

stddraw.square(0.5 - half_length, 0.5 - half_length, half_length)
stddraw.filledCircle(0.5 - half_length, 0.5 - half_length, 0.005)

stddraw.show()