#-------------
# final/glass_copy.py
# Andrei Suslov
# CISC 120-91
#-------------

import random
from picture import Picture
import sys

def glass_copy(pic, fuzz):
    """
    Applies a glass filter to an image, creating a "fuzzy" effect by randomizing the pixel positions.
    
    Parameters:
    pic (Picture): The input Picture object.
    fuzz (int): The maximum distance from the current pixel to select a random pixel's color.
    
    Returns:
    Picture: A new Picture object with the glass filter applied.
    """
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

def main():
    if len(sys.argv) != 3:
        print("Usage: python glass.py <image_path> <fuzz>")
        sys.exit(1)

    image_path = sys.argv[1]
    fuzz = int(sys.argv[2])

    pic = Picture(image_path)
    new_pic = glass_copy(pic, fuzz)

    new_image_path = f"glass_{fuzz}_{image_path}"
    new_pic.save(new_image_path)
    print(f"Filtered image saved as {new_image_path}")

if __name__ == "__main__":
    main()