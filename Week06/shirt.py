import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():

    #check command line arguments
    if len(sys.argv) == 3:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

    ext = (".jpg", ".jpeg", ".png")

    #check extensions
    if splitext(infile.lower())[1] not in ext:
         sys.exit(f"Invalid input")
    elif splitext(outfile.lower())[1] not in ext:
        sys.exit(f"Invalid output")
    elif splitext(infile.lower())[1] != splitext(outfile.lower())[1]:
        sys.exit(f"Input and output have different extensions")

    #open input image, resize/crop, and overlay shirt on it
    try:
        with Image.open("shirt.png") as shirt, Image.open(infile) as before:
            size = shirt.size
            before = ImageOps.fit(before, size)
            before.paste(shirt, shirt)
            before.save(outfile)
    except(FileNotFoundError):
        sys.exit("Input does not exist")

if __name__ == "__main__":
     main()




