''' Reads an image (320x240), converts to grayscale
    then resizes to 160x120 and 640x480'''

import cv2 as cv

# Reads an image 
image = cv.imread('image.jpg')

# Converts to grayscale
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# displays the input image
cv.imshow('Input Image', grayscale_img)
cv.waitKey(0)

# resizes to 160x120
img_160_120 = cv.resize(grayscale_img, (160, 120))
img_640_480 = cv.resize(grayscale_img, (640, 480))

# displays the redimensions
cv.imshow('160x120 image', img_160_120)
cv.imshow('640x480 image', img_640_480)
cv.waitKey(0)

# Saves the results
cv.imwrite('image_160_120.jpg', img_160_120)
cv.imwrite('image_640_480.jpg', img_640_480)