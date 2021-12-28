# rename.py
# rename files in a folder

# Rename all files in a folder:
import os
import cv2
import glob
import argparse

# Get the path to the images:
parser = argparse.ArgumentParser(description='Rename fils.')
parser.add_argument("-p","--path2imgs", help="Img location", default='/Users/felipeparodi/Desktop/MonkeyImgs/')
args = parser.parse_args()
fold = glob.gob(args.path2imgs)
 
# folder path and destination
input_dir = '/Users/felipeparodi/Desktop/MonkeyImgs/*.jpg'
fold = glob.glob(input_dir)
 
# loop through the directory to rename all the files
for count, filename in enumerate(fold):
        new ="frame_" + str(count) + '.jpg'  # new file name
        src = os.path.join(input_dir[:-5], filename)  # file source
        dst = os.path.join(input_dir[:-5], new)  # file destination
        # rename all the file
        os.rename(src, dst)
