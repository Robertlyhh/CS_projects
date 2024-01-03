import sys
from PIL import Image

try:
    # Get the image path from the command-line argument
    image_path = sys.argv[1]

    # Open the image
    with Image.open(image_path) as im:

        # Ensure the image is loaded
        im.load()

        # Get image information
        print(f"{image_path} {im.format} {im.size}x{im.mode}")

        # Define the region to be cropped (replace these values accordingly)
        box = (100, 100, 300, 300)

        # Check if the box coordinates are within the image boundaries
        if all(0 <= coord <= size for coord, size in zip(box, im.size)):

            # Crop the image
            region = im.crop(box)

            # Save or do something with the cropped image
            region.save('/Users/tengli/Desktop/cropped_image.png')

            print("Cropped image saved successfully.")
        else:
            print("Error: The specified crop box is outside the image boundaries.")

except Exception as e:
    print(f"An error occurred: {e}")

