''' Reads an image, converts to grayscale, applies  
    limiarization and show the results '''

import cv2 as cv

# Reads an image 
image = cv.imread('image.jpg')

# Converts to grayscale
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# displays the input image
cv.imshow('Input Image', grayscale_img)
cv.waitKey(0)

# applies the threshold
ret, threshold_image = cv.threshold(grayscale_img, 70, 255, cv.THRESH_BINARY)

# displays the result of the threshold
cv.imshow('Threshold Result', threshold_image)
cv.waitKey(0)

# Saves the results
cv.imwrite('threshold_result.jpg', threshold_image)
