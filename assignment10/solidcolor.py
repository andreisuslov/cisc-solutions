# CISC 120-91
# assignment10/solidcolor.py
# Andrei Suslov
# to test this file, run `python solidcolor.py 30 58 5`

"""
1. Function `create_colored_picture(red, green, blue)`:
   - Creates a solid color image with the specified RGB values.
   - Returns the colored `Picture` object.
2. Function `main()`:
   - Checks if the correct number of command-line arguments (3) are provided. If not, it displays the usage information and exits with status code 1.
   - Parses the red, green, and blue values from the command-line arguments.
   - Validates that the color values are within the valid range (0-255).
   - Calls the `create_colored_picture()` function to create the colored picture.
   - Sets the canvas size for drawing to 256x256 pixels.
   - Displays the colored picture using `stddraw.picture()` and shows it using `stddraw.show()`.
"""

import sys
from picture import Picture
from color import Color
import stdio
import stddraw

def create_colored_picture(red, green, blue):
    # create a Picture filled with the specified color
    color = Color(red, green, blue)
    picture = Picture(256, 256)
    for col in range(256):
        for row in range(256):
            picture.set(col, row, color)
    return picture

def main():
    if len(sys.argv) != 4:
        # Display usage information
        stdio.writeln("Usage: python solidcolor.py <red> <green> <blue>")
        sys.exit(1)

    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        # check if color values are within the valid range
        stdio.writeln("Color values must be between 0 and 255.")
        sys.exit(1)

    colored_picture = create_colored_picture(red, green, blue)

    # display the picture
    stddraw.setCanvasSize(256, 256)
    stddraw.picture(colored_picture)
    stddraw.show()

if __name__ == "__main__":
    main()
