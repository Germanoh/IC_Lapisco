'''
Reads an image from a file, shows it then saves it
'''

import cv2 as cv

''' reads an image '''
img = cv.imread('image.jpg')

''' shows the image '''
cv.imshow("Display window", img)

''' wait for a key to be pressed'''
key = cv.waitKey(0)

''' saves the image '''
cv.imwrite("saved_image.jpg", img)



