from PIL import Image
import os
filename = input("Enter the location of image to be processed: ")
filename = filename.strip('"').strip("'")

dirPath ,imageName = os.path.split(filename)
imageNameWithoutExt, imageExt = os.path.splitext(imageName)

with Image.open(filename) as img:
    img.load()
img.show()
# cropping tool ko lagi I need to take 4 parameters for 4 corners of the picture
# the picture's location should be inserted by the user
print("1. Crop\n2. Decrease Resolution\n3. Image Manipulation\n0. Exit\n")
a = input("Enter your choice: ")

def crop_img(img):
    print("Crop it is.")
    print("The crop size is refrenced from the top of the image and should be entered in pixels")
    left = int(input("Enter pixels from left: "))
    top = int(input("Enter pixels from top: "))
    right = int(input("Enter pixels from right: "))
    bottom = int(input("Enter pixels from bottom: "))
    cropped_img = img.crop((left,top,right,bottom))
    cropped_img.show()
    cropped_img.save(f"{dirPath}/{imageNameWithoutExt}_cropped{imageExt}")

match a:
    case "1":
        crop_img(img)
    case "2":
        print("Resolution Decrease")
    case "3":
        print("Image Manipulation")
    case _:
        print("Invalid Choice. Exiting")