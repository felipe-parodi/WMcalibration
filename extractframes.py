# Extract frames from multiple videos in desktop folder:
import cv2
import glob
import argparse

parser = argparse.ArgumentParser(description='Frame extraction.')


parser.add_argument("-p","--path2vids", help="Video location", default='/Users/felipeparodi/Desktop/MonkeyImgs/*.mp4')
args = parser.parse_args()

fold = glob.glob('/Users/felipeparodi/Desktop/MonkeyImgs/*.mp4')

for f in fold:
    cap = cv2.VideoCapture(str(f))
    count=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('/Users/felipeparodi/Desktop/MonkeyImgs/frame{:d}.jpg'.format(count),frame)
            print('frame{:d}.jpg'.format(count))
            count += 30 # skip 30 frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        else:
            break