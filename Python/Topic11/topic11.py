'''
Reads an image with a black square on the center and a white background, converts
to grayscale and draws a circle on the centroid of the black square.
'''

import cv2 as cv
import numpy as np

# reads an image
image = cv.imread('C:/Users/germa/Documents/Lapisco/IC_Lapisco/Python/Topic11/image.jpg')

# converts to grayscale and display on screen
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Input image", grayscale_image)
key = cv.waitKey(0)

# extracts the dimensions of the grayscale image and stores in a matrix of same size
width, height = grayscale_image.shape[:2]
new_image = np.zeros((width, height), dtype=np.uint8)

for row in range(height):
    for col in range(width):
        new_image[row, col] = grayscale_image[row, col]

# gets the points of the square
yc = 0
xc = 0
count = 0

for y in range(width):
    for x in range(height):
        if new_image[y][x] == 0:
            yc += y
            xc += x
            count += 1

# gets the coordinates of the centroid
xc = int(xc / count)
yc = int(yc / count)

# draws a circle in the centroid of the new image and displays on screen 
cv.circle(new_image, (xc, yc), 5, (255, 255, 255), -1)
cv.imshow("Centroid", new_image)
k = cv.waitKey(0)

# saves the centroid image
cv.imwrite('centroid.jpg', new_image)