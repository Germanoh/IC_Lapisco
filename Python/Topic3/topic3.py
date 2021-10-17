import cv2 as cv

# read a RGB image
img = cv.imread('image.jpg')

# separates each RGB channel
blue_channel, green_channel, red_channel = cv.split(img)

# shows each channel individually
cv.imshow('Blue Channel', blue_channel)
cv.imshow('Green Channel', green_channel)
cv.imshow('Red Channel', red_channel)

cv.waitKey(0)

# saves the results
cv.imwrite('blue_channel.jpg', blue_channel)
cv.imwrite('green_channel.jpg', green_channel)
cv.imwrite('red_channel.jpg', red_channel)
