from PIL import Image, ImageOps
import sys


def main():

    with Image.open(sys.argv[1]) as image, Image.open("shirt.png") as im:
        size = im.size
        image_resized = ImageOps.fit(image, size)
        image_resized.save(sys.argv[2])


        image_resized.paste(im,(0,0),im)
        image_resized.save(sys.argv[2])


if __name__ == "__main__":
    main()