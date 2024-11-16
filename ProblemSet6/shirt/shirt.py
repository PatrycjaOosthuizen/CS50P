import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    # Try open the image
    try:
        image = Image.open(sys.argv[1])
    # If the image won't open means the image doesn't exist - rise FileNotFoundError
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open shirt image
    shirt_image = Image.open("shirt.png")
    # Get the size of the shirt image
    size = shirt_image.size
    # Resize muppet image to fit the shirt
    muppet_photo = ImageOps.fit(image, size)
    # Paste shirt on muppet
    muppet_photo.paste(shirt_image, shirt_image)
    # Create and save output image
    muppet_photo.save(sys.argv[2])

def check_command_line_arg():
    # Check lenght of elements entered in the command line
    if len(sys.argv) < 3:
       sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
       sys.exit("Too many command-line arguments")
    file_extension_1 = splitext(sys.argv[1])
    file_extension_2 = splitext(sys.argv[2])
    # Check if extension exist in extension list, it is an image file [".jpg", ".jepg", ".png"]
    if check_extensions(file_extension_1[1]) == False:
        sys.exit("Invalid input")
    if check_extensions(file_extension_2[1]) == False:
        sys.exit("Invalid output")
    # Check if extensions of both files are different
    if file_extension_1[1].lower() != file_extension_2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extensions(file):
    if file in [".jpg", ".jepg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()
