# Convert png in folder to jpg

# Convert png to jpg:
import os
import cv2
import glob
import argparse
from PIL import Image

# Get the path to the images:
parser = argparse.ArgumentParser(description='Convert to jpg.')
parser.add_argument("-p","--path2imgs", help="Video location", default='/Users/felipeparodi/Desktop/MonkeyImgs/')
args = parser.parse_args()

# Path to images
input_dir = glob.gob(args.path2imgs)
# input_dir = '/Users/felipeparodi/Desktop/MonkeyImgs/*.png'
names = glob.glob(input_dir)

# Initalize the counter:
counter = 0

# Loop through the images:
for name in names:
    # Get the name of the image:
    img = Image.open(input_dir + name) # open color image
    name = name.split(".") # split the filename
    # Convert to jpg:
    if name[-1] == "png":
        name[-1] = "jpg" # replace the extension
        name = str.join(".", name) # reassemble the filename
        save_path = input_dir + name # create path to save image
        img = img.convert('RGB') # convert to RGB
        img.save(save_path) # save the image
        counter += 1 # increment counter
        # os.remove(name) # remove the original image
    else:
        continue