# create and save charucoboard pattern

'''
This script creates a charucoboard pattern and saves it to a file.

If you're too lazy to create the pattern yourself, you can use the
https://markrmakr.herokuapp.com/charuco_board tool.

For a list of aruco dictionaries, see here: 
https://docs.opencv.org/3.4/dc/df7/dictionary_8hpp.html
'''
import cv2
import matplotlib.pyplot as plt

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
board = cv2.aruco.CharucoBoard_create(8,8,.025,.0125,dictionary)
img = board.draw((200*8,200*8))

plt.imshow(img, cmap='gray')
plt.savefig('./charucowscript.svg')
plt.show()