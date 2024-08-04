from PIL import Image # type: ignore
from Functions.GUIrequest import open_image_file

def color_to_black(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error while opening image: ",e)    
    if image.mode != "RGB":
        image = image.convert("RGB")

    #Get the images pixels
    pixels = image.load()
    #Get the image height and width
    height,width = image.size


    for y in range(width):
        for x in range(height):
            r, g, b = pixels[x, y]
            
            # Compute the grayscale value
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            
            # Set the pixel to the grayscale value
            pixels[x, y] = (gray, gray, gray)

    return image
try:
    image = color_to_black(open_image_file())
    if image:
        image.show()
    else:
        print("Error while displaying image")
except Exception as e:
    print("Error while changing image: ",e)