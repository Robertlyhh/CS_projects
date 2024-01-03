import os, sys
from PIL import Image


def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im


def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im


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
        region = roll(im, 180)

        region.save('/Users/tengli/Desktop/rolled_image.png')

        print("Cropped image saved successfully.")


except Exception as e:
    print(f"An error occurred: {e}")

