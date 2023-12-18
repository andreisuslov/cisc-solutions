# --------------------------------------------------
# lab5/scale_test.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------
# to test this file, run `python scale_test.py image.jpg 2.0`

"""

Explanation of scale_test.py:

1. The program is designed to scale an image by a given factor.
2. It imports necessary modules: sys for command line arguments, picture for image processing, and stddraw for displaying images.
3. The 'scale' function:
   - Takes an image and a scale factor as inputs.
   - Calculates the new width and height based on the scale factor.
   - Creates a new scaled image with the calculated dimensions.
   - Iterates over each pixel of the new image, computes corresponding pixels from the original image, and sets the color.
   - Returns the scaled image.
4. The 'main' function:
   - Retrieves the filename and scale factor from command line arguments.
   - Loads the original image from the specified file.
   - Calls the 'scale' function to get the scaled image.
   - Sets up the canvas size using stddraw to match the dimensions of the scaled image.
   - Displays the scaled image using stddraw.
5. The program is executed as a script, running the 'main' function if it is the main module.
"""

import sys
from picture import Picture
import stddraw


# scale the image by a given scale factor
def scale(image, scale_factor):
    width = round(image.width() * scale_factor)
    height = round(image.height() * scale_factor)
    scaled_image = Picture(width, height)

    for col in range(width):
        for row in range(height):
            source_col = int(col // scale_factor)
            source_row = int(row // scale_factor)
            color = image.get(source_col, source_row)
            scaled_image.set(col, row, color)

    return scaled_image

def main():
    file_name = sys.argv[1]
    scale_factor = float(sys.argv[2])

    original_image = Picture(file_name)

    # Scale the original image
    scaled_image = scale(original_image, scale_factor)

    # Display the scaled image
    stddraw.setCanvasSize(scaled_image.width(), scaled_image.height())
    stddraw.picture(scaled_image)
    stddraw.show()

if __name__ == "__main__":
    main()
