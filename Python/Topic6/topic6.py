''' Reads an image, converts to grayscale, applies  
    canny filter and show the results '''

import cv2 as cv

# Reads an image 
image = cv.imread('image.jpg')

# Converts to grayscale
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# displays input image
cv.imshow('Input Image', grayscale_img)
cv.waitKey(0)

# applies canny filter
canny_image = cv.Canny(grayscale_img, 80, 100)

# displays canny filter results
cv.imshow('Canny Filter Result', canny_image)
cv.waitKey(0)

# Saves the results
cv.imwrite('canny_filter_result.jpg', canny_image)
