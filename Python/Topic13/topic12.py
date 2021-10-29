''' Topic12: Asks for an image, turns to grayscale makes an static matrix
    with the same dimensions of the image and applies a sobel filter on the
    new image '''

import cv2 as cv
import numpy as np

# reads and display input image
image = cv.imread('image.jpg')

cv.imshow('Input image', image)
cv.waitKey(0)

grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale image', grayscale_image)
cv.waitKey(0)


