''' Reads an image, converts to grayscale, applies blur and 
    media filter and show the results '''

import cv2 as cv

# Reads an image 
image = cv.imread('image.jpg')

# Converts to grayscale
grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# displays input image
cv.imshow('Input Image', grayscale_img)
cv.waitKey(0)

# applies median and blur filter
blur_image = cv.blur(grayscale_img, ksize=(5, 5))
median_image = cv.medianBlur(grayscale_img, ksize=5)

# displays blur and median filter results
cv.imshow('Blur Filter Result', blur_image)
cv.imshow('Median Filter Result', median_image)
cv.waitKey(0)

# Saves the results
cv.imwrite('blur_image.jpg', blur_image)
cv.imwrite('median_image.jpg', median_image)
