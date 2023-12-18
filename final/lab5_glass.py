# --------------------------------------------------
# lab5_glass.py
# Andrei Suslov
# CISC 120-91
# --------------------------------------------------

# to test this file, run `python lab5_glass.py image.jpg 2 2 0.5 0.5`

import sys
from picture import Picture
import stddraw
from glass import glass_inplace_new # import the glass filter module



def scale(source, scale_factor):
    """Scales the source image by the given scale factor."""
    # Calculate new dimensions
    width = int(source.width() * scale_factor)
    height = int(source.height() * scale_factor)
    
    # Create new picture and set pixels
    target = Picture(width, height)
    for col in range(width):
        for row in range(height):
            color = source.get(int(col / scale_factor), int(row / scale_factor))
            target.set(col, row, color)
    
    return target

def extract_image(scaled_image, center_x_ratio, center_y_ratio, orig_width, orig_height):
    """Extracts a portion of the scaled image to create a zoomed-in view."""
    # Calculate center point
    center_x = int(center_x_ratio * scaled_image.width())
    center_y = int(center_y_ratio * scaled_image.height())

    # Calculate range to extract
    start_x = max(0, center_x - orig_width // 2)
    end_x = min(scaled_image.width(), center_x + orig_width // 2)
    start_y = max(0, center_y - orig_height // 2)
    end_y = min(scaled_image.height(), center_y + orig_height // 2)

    # Create new picture and set pixels
    zoomed_image = Picture(end_x - start_x, end_y - start_y)
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            color = scaled_image.get(x, y)
            zoomed_image.set(x - start_x, y - start_y, color)
    
    return zoomed_image

def main():
    if len(sys.argv) != 6:
        print("Usage: python lab5_glass.py <filename> <scale_factor> <fuzz_factor> <center_x> <center_y>")
        sys.exit(1)

    filename = sys.argv[1]
    scale_factor = float(sys.argv[2])
    fuzz_factor = float(sys.argv[3])
    center_x_ratio = float(sys.argv[4])
    center_y_ratio = float(sys.argv[5])

    try:
        source = Picture(filename)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

    scaled_image = scale(source, scale_factor)
    zoomed_image = extract_image(scaled_image, center_x_ratio, center_y_ratio, source.width(), source.height())

    # Apply the glass filter with a given fuzz factor
    glass_inplace_new(zoomed_image, fuzz_factor)

    # Display the glass-filtered zoomed image
    stddraw.setCanvasSize(zoomed_image.width(), zoomed_image.height())
    stddraw.picture(zoomed_image)
    stddraw.show()

if __name__ == "__main__":
    main()