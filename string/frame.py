from PIL import Image

def displayImage(image_file, frame, string):
    image = Image.open(image_file)

    for x in range(string.length):
        pixel = image.getPixel(x, frame)
        string[x] = (pixel[0], pixel[1], pixel[2])