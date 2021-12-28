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
input_dir = glob.gob(args.path2imgs)

# input_dir = '/Users/felipeparodi/Desktop/MonkeyImgs/'
# cast to list to avoid error:
fold = list(glob.glob(input_dir+'*.png'))
for f in fold:
    # only jpg files:
    if os.path.splitext(f)[1] == '.png':
        img = Image.open(f)
        img.save(f.replace('.png','.jpg'))
        os.remove(f)