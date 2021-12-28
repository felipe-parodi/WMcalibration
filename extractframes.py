# Extract frames from multiple videos in desktop folder:
import cv2
import glob
import argparse

# Get the path to the videos:
parser = argparse.ArgumentParser(description='Frame extraction.')
parser.add_argument("-p","--path2vids", help="Video location", default='/Users/felipeparodi/Desktop/MonkeyImgs/*.mp4')
args = parser.parse_args()

# fold = glob.glob('/Users/felipeparodi/Desktop/MonkeyImgs/*.mp4')
# Use argument passed by user:
fold = glob.glob(args.path2vids)

# Loop through the videos:
for idx, f in enumerate(fold):
    cap = cv2.VideoCapture(str(f))
    count=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Name frames with the video number and the frame number:
            cv2.imwrite('/Users/felipeparodi/Desktop/MonkeyImgs/cam{:d}_{:d}.jpg'.format(idx,count),frame)
            print('cam{:d}_{:d}.jpg'.format(idx,count))
            count += 30 # skip 30 frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        else:
            break