import os
filename = input("Enter the location of image to be processed: ")

dirPath ,imageName = os.path.split(filename)
imageNameWithoutExt, imageExt = os.path.splitext(imageName)

print(f"Image Name with extension:{imageName}")
print(f"Image Name without extension :{imageNameWithoutExt}")
print(f"extension :{imageExt}")
# print(f"Image Name without extension :{imageNameWithoutExt}")

