import random
import sys
from picture import Picture

def glass_inplace_new(pic, fuzz):
    """
    Applies a glass filter to an image in-place, creating a "fuzzy" effect by randomizing the pixel positions.
    This implementation fixes the issue of pixels potentially being altered multiple times.
    
    Parameters:
    pic (Picture): The input Picture object to be altered.
    fuzz (int): The maximum distance from the current pixel to select a random pixel's color.
    """
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

def main():
    # Check if the correct number of command-line arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python glass_inplace_new.py <image_path> <fuzz>")
        sys.exit(1)
    
    # Parse command-line arguments
    image_path = sys.argv[1]
    fuzz = int(sys.argv[2])

    # Load the picture from the file
    try:
        pic = Picture(image_path)
    except FileNotFoundError:
        print("Error: The specified image file could not be found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        sys.exit(1)

    # Apply the glass filter in-place
    glass_inplace_new(pic, fuzz)

    # Save the altered image
    try:
        new_image_path = f"glass_inplace_new_{fuzz}_{image_path}"
        pic.save(new_image_path)
        print(f"Filtered image saved as {new_image_path}")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Example usage (commented out):
# To run this script from the command line, use the following format:
# python glass_inplace_new.py <path_to_image> <fuzz_value>
# Example:
# python glass_inplace_new.py example.jpg 5