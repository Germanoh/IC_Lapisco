''' Reads an image, separates into HSV channels 
    and display each one separately'''

import cv2 as cv

# Reads an RGB image
image = cv.imread('image.jpg')

# Transforms to HSV 
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Split the HSV channels
h_channel, s_channel, v_channel = cv.split(hsv_image)

# Shows the HSV image and its channels
cv.imshow('HSV image', hsv_image)
cv.imshow('H Channel', h_channel)
cv.imshow('S Channel', s_channel)
cv.imshow('V Channel', v_channel)

cv.waitKey(0)

# Saves the results
cv.imwrite('hsv_image.jpg', hsv_image)
cv.imwrite('h_channel.jpg', h_channel)
cv.imwrite('s_channel.jpg', s_channel)
cv.imwrite('v_channel.jpg', v_channel)