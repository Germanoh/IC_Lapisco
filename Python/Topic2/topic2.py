''' reads a colored image, transforms to grayscale, 
    display on screen, saves the grayscale image '''

import cv2 as cv

# Read a RGB image
img = cv.imread('C:/Users/germa/Documents/Lapisco/IC_Lapisco/Python/Topic2/image.jpg')

# transforms to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# display grayscale image
cv.imshow("Display window", grayscale_img)
key = cv.waitKey(0)

# save the result
cv.imwrite('grayscale_image.jpg', grayscale_img)