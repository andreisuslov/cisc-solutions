# MODULE NAME
"""
# --------------------------------------------------
# glass.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------
"""

# to test this module, run `python glass.py image.jpg 8`

# DESCRIPTION
"""
# --------------------------------------------------
# A module with functions that are designed 
# to help deal with fuzziyng pictures.
# --------------------------------------------------
"""

# FUNCTIONS

# -------------------------------------------------------

import random
import sys
import stddraw
from picture import Picture

"""
glass_copy(pic, fuzz)
Applies a glass filter to an image, creating a "fuzzy" effect by randomizing the pixel positions.

Parameters:
pic (Picture): The input Picture object.
fuzz (int): The maximum distance from the current pixel to select a random pixel's color.

Returns:
Picture: A new Picture object with the glass filter applied.
"""
def glass_copy(pic, fuzz):
    # Create a new Picture object of the same size as the input Picture
    new_pic = Picture(pic.width(), pic.height())

    # Iterate over each pixel in the picture
    for i in range(pic.width()):
        for j in range(pic.height()):
            # Randomly select a nearby pixel within fuzz distance
            random_x = max(0, min(pic.width() - 1, i + random.randint(-fuzz, fuzz)))
            random_y = max(0, min(pic.height() - 1, j + random.randint(-fuzz, fuzz)))
            
            # Get the color of the randomly selected pixel
            c = pic.get(random_x, random_y)
            
            # Set the color of the current pixel to the color of the randomly selected pixel
            new_pic.set(i, j, c)

    return new_pic

"""
glass_inplace(pic, fuzz)
Applies a glass filter to an image in-place, creating a "fuzzy" effect by randomizing the pixel positions.

Parameters:
pic (Picture): The input Picture object to be altered.
fuzz (int): The maximum distance from the current pixel to select a random pixel's color.

This function does not return anything as it modifies the input Picture object directly.
"""
def glass_inplace(pic, fuzz):
    width, height = pic.width(), pic.height()
    
    # Iterate over each pixel in the picture
    for i in range(width):
        for j in range(height):
            # Randomly select a nearby pixel within fuzz distance
            random_x = max(0, min(width - 1, i + random.randint(-fuzz, fuzz)))
            random_y = max(0, min(height - 1, j + random.randint(-fuzz, fuzz)))
            
            # Get the color of the randomly selected pixel
            random_color = pic.get(random_x, random_y)
            
            # Set the color of the current pixel to the color of the randomly selected pixel
            pic.set(i, j, random_color)


"""
glass_inplace_new(pic, fuzz)
Applies a glass filter to an image in-place, creating a "fuzzy" effect by randomizing the pixel positions.
This implementation fixes the issue of pixels potentially being altered multiple times.

Parameters:
pic (Picture): The input Picture object to be altered.
fuzz (int): The maximum distance from the current pixel to select a random pixel's color.
"""
def glass_inplace_new(pic, fuzz):
    width, height = pic.width(), pic.height()
    # Create a temporary Picture object to store the new colors
    temp_pic = Picture(width, height)

    # Iterate over each pixel in the picture to fill the temporary picture with new colors
    for i in range(width):
        for j in range(height):
            # Randomly select a nearby pixel within fuzz distance
            random_x = max(0, min(width - 1, i + random.randint(-fuzz, fuzz)))
            random_y = max(0, min(height - 1, j + random.randint(-fuzz, fuzz)))
            
            # Get the color of the randomly selected pixel
            random_color = pic.get(random_x, random_y)
            
            # Store the color in the temporary picture
            temp_pic.set(i, j, random_color)

    # Apply the new colors from the temporary picture to the original picture
    for i in range(width):
        for j in range(height):
            color = temp_pic.get(i, j)
            pic.set(i, j, color)



# a helper function to display images with text
def show_with_text(picture, text, timeout):
    stddraw.clear()  # Clear the previous drawing
    stddraw.picture(picture, 0.5, 0.5)  # Draw the picture in the canvas
    # Set the text color
    stddraw.setPenColor(stddraw.BLACK)
    # Set the font size to make the text bigger
    stddraw.setFontSize(30)
    # Draw the text in the middle of the top 200 pixels of the canvas
    stddraw.text(0.5,0.9, text)
    stddraw.show(timeout)


if __name__ == "__main__":
    # Test code
    if len(sys.argv) != 3:
        print("Usage: python glass.py <image_path> <fuzz>")
        sys.exit(1)

    image_path = sys.argv[1]
    fuzz = int(sys.argv[2])
    timeout = 5000

    # Prepare the stddraw canvas before showing any images
    original_pic = Picture(image_path)
    # Set canvas size with additional space for the text
    stddraw.setCanvasSize(original_pic.width() + 200, original_pic.height() + 200)

    # Load and apply glass_copy
    copied_pic = glass_copy(original_pic, fuzz)
    show_with_text(copied_pic, "glass_copy", timeout)

    # Reload the original picture and apply glass_inplace
    original_pic = Picture(image_path)
    glass_inplace(original_pic, fuzz)
    show_with_text(original_pic, "glass_inplace", timeout)

    # Reload the original picture and apply glass_inplace_new
    original_pic = Picture(image_path)
    glass_inplace_new(original_pic, fuzz)
    show_with_text(original_pic, "glass_inplace_new", timeout)
