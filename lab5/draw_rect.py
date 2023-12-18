# --------------------------------------------------
# lab5/draw_rect.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------

"""

This Python script, 'draw_rect.py', performs the following functions:

1. Import required modules: sys for command-line arguments, stddraw for drawing, and Picture from a custom module.

2. Define a function 'scale' to scale an image:
   - Takes a source image and a scale factor as inputs.
   - Calculates the new width and height based on the scale factor.
   - Creates a new Picture object with the calculated dimensions.
   - Copies pixels from the source image to the scaled image based on the scale factor.

3. Define a function 'validate_input' to validate command-line arguments:
   - Ensures the correct number of arguments are provided.
   - Converts scale factor and center coordinates from strings to floats.
   - Exits the program with an error message if inputs are invalid.

4. Define a function 'setup_canvas' to set up the drawing canvas:
   - Sets the canvas size to match the image dimensions.
   - Configures the coordinate system for drawing.

5. Define a function 'draw_image' to draw the image and rectangle:
   - Displays the scaled image.
   - Draws a filled circle (point) at the specified center coordinates.
   - Draws a rectangle around the center point with the width and height of the original image.

6. Define the 'main' function:
   - Gets and validates the command-line arguments.
   - Loads the image from the provided filename.
   - Scales the image using the provided scale factor.
   - Calculates absolute center coordinates for the rectangle.
   - Sets up the canvas and draws the image with the rectangle.
   - Shows the final drawing on the screen.

7. Execute the 'main' function if the script is run as a standalone program.
"""

import sys
import stddraw
from picture import Picture

def scale(source, scale_factor):
    """Scale the source image by the specified scale factor."""
    target_width = round(source.width() * scale_factor)
    target_height = round(source.height() * scale_factor)
    target = Picture(target_width, target_height)

    for col in range(target_width):
        for row in range(target_height):
            source_col = col * source.width() // target_width
            source_row = row * source.height() // target_height
            target.set(col, row, source.get(source_col, source_row))
    return target

def validate_input(args):
    """ Validate the input arguments. """
    if len(args) != 5:
        print("Usage: python draw_rect.py <filename> <scale_factor> <center_x> <center_y>")
        sys.exit(1)
    try:
        scale_factor = float(args[2])
        center_x_ratio = float(args[3])
        center_y_ratio = float(args[4])
    except ValueError:
        print("Error: Scale factor and center coordinates must be numbers.")
        sys.exit(1)
    return args[1], scale_factor, center_x_ratio, center_y_ratio

def setup_canvas(image):
    """ Set up the drawing canvas and scales. """
    stddraw.setCanvasSize(image.width(), image.height())
    stddraw.setXscale(0, image.width())
    stddraw.setYscale(0, image.height())

def draw_image(image, center_x, center_y, rect_width, rect_height):
    """ Draw the image, point, and rectangle. """
    stddraw.picture(image)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(center_x, center_y, 5)  # Drawing a point
    stddraw.rectangle(center_x - rect_width // 2, center_y - rect_height // 2, rect_width, rect_height)  # Drawing a rectangle

def main():
    filename, scale_factor, center_x_ratio, center_y_ratio = validate_input(sys.argv)
    
    try:
        source = Picture(filename)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

    scaled_image = scale(source, scale_factor)

    center_x = int(center_x_ratio * scaled_image.width())
    center_y = int(center_y_ratio * scaled_image.height())

    setup_canvas(scaled_image)
    draw_image(scaled_image, center_x, center_y, source.width(), source.height())
    stddraw.show()

if __name__ == "__main__":
    main()
