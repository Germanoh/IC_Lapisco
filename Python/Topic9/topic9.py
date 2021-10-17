''' Reads an image, converts to gray, extracts the values of each pixel and
    to a matrix and outputs all the value from the matrix in a text file '''

import cv2 as cv
import numpy as np

# Reads an image 
image = cv.imread('image.jpg')

# Converts to grayscale
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# displays the input image
cv.imshow('Input Image', grayscale_img)
cv.waitKey(0)

# Creates a matrix with the same dimensions of the grayscale image
width, height = grayscale_img.shape[:2]
matrix = np.zeros((width, height), dtype=np.uint8)

# saves the value of each pixel in a matrix
for row in range(height):
    for col in range(width):
        matrix[row][col] = grayscale_img[row][col]

# Creates a file to receive the pixel values of the image
try:
    file = open('pixel_values.txt', 'w')
except:
    print("Couldn't open file")

# Writes the value of each pixel of the grayscale image to a file
for i in range(height):
    for j in range(width):
        file.write("%s " % str(matrix[i][j]))