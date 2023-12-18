# --------------------------------------------------
# lab5/zoom.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------

"""

This Python script, 'zoom.py', is designed to zoom into a specific area of an image. Here's what each part of the code does:

1. Import necessary modules: `sys` for command-line arguments, `picture` for image processing, and `stddraw` for displaying images.

2. Define a function `scale(source, scale_factor)`:
   - Scales the source image by a given scale factor.
   - Calculates the new width and height based on the scale factor.
   - Creates a new `Picture` object for the scaled image.
   - Iterates over each pixel of the target image, maps it to the corresponding pixel in the source image, and sets the color.

3. Define a function `extract_image(scaled_image, rel_x, rel_y, orig_width, orig_height)`:
   - Extracts a portion of the scaled image to create a zoomed-in view.
   - Adjusts the coordinate system for the y-axis due to different conventions in image processing.
   - Calculates the center and lower left corner of the area to be extracted based on the provided relative coordinates and original image dimensions.
   - Creates a new picture for the zoomed-in area and sets the pixels accordingly.

4. Define a `main` function for script execution:
   - Checks if the correct number of command-line arguments is provided.
   - Reads the filename, scale factor, and center coordinates from the command-line arguments.
   - Loads the image from the file and checks for errors.
   - Calls the `scale` function to scale the original image.
   - Calls the `extract_image` function to extract the zoomed-in portion.
   - Sets the canvas size and displays the zoomed-in image using `stddraw`.

5. The `if __name__ == "__main__":` block to ensure that the `main` function is called when the script is executed directly.
"""

import sys
from picture import Picture
import stddraw

# to test, run `python zoom.py miranda.jpg 2 0.65 0.70`

def scale(source, scale_factor):
    """ Scale the source image by the specified scale factor. """
    target_width = round(source.width() * scale_factor)
    target_height = round(source.height() * scale_factor)
    target = Picture(target_width, target_height)

    for col in range(target_width):
        for row in range(target_height):
            source_col = col * source.width() // target_width
            source_row = row * source.height() // target_height
            target.set(col, row, source.get(source_col, source_row))
    return target


def extract_image(scaled_image, rel_x, rel_y, orig_width, orig_height):
    """ Extract a portion of the scaled image to create a zoomed-in view. """
    scaled_width = scaled_image.width()
    scaled_height = scaled_image.height()

    # Adjust the coordinate system for the y-axis
    rel_y = 1 - rel_y

    # Calculate the absolute center coordinates in the scaled image
    center_x = int(rel_x * scaled_width)
    center_y = int(rel_y * scaled_height)

    # Calculate the lower left corner of the extracted area
    start_x = max(center_x - orig_width // 2, 0)
    start_y = max(center_y - orig_height // 2, 0)

    # Create a new picture for the zoomed-in area
    zoomed_image = Picture(orig_width, orig_height)

    for col in range(orig_width):
        for row in range(orig_height):
            source_col = min(start_x + col, scaled_width - 1)
            source_row = min(start_y + row, scaled_height - 1)
            color = scaled_image.get(source_col, source_row)
            zoomed_image.set(col, row, color)

    return zoomed_image

import sys
from picture import Picture
import stddraw

# Include the scale function defined earlier

def main():
    if len(sys.argv) != 5:
        print("Usage: python zoom.py <filename> <scale_factor> <center_x> <center_y>")
        sys.exit(1)

    filename = sys.argv[1]
    scale_factor = float(sys.argv[2])
    center_x_ratio = float(sys.argv[3])
    center_y_ratio = float(sys.argv[4])

    try:
        source = Picture(filename)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

    scaled_image = scale(source, scale_factor)

    # Extract the zoomed-in image
    zoomed_image = extract_image(scaled_image, center_x_ratio, center_y_ratio, source.width(), source.height())

    # Display the zoomed-in image
    stddraw.setCanvasSize(zoomed_image.width(), zoomed_image.height())
    stddraw.picture(zoomed_image)
    stddraw.show()

if __name__ == "__main__":
    main()

def main():
    file_name = sys.argv[1]
    scale_factor = float(sys.argv[2])
    center_x_ratio = float(sys.argv[3])
    center_y_ratio = float(sys.argv[4])
    original_image = Picture(file_name)
    scaled_image = scale(original_image, scale_factor) # scale the original image    
    center_x = int(center_x_ratio * scaled_image.width()) # calculate the center coordinates for zooming
    center_y = int(center_y_ratio * scaled_image.height())
    # extract the zoomed subimage
    zoomed_image = extract_image(scaled_image, center_x, center_y, original_image.width(), original_image.height())
    # display the zoomed image
    stddraw.picture(zoomed_image)
    stddraw.show()

if __name__ == "__main__":
    main()
