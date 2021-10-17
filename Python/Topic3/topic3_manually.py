''' Opens a colored image, extracts each one of it's channels then displays
    and saves them '''

import cv2 as cv
import numpy as np

def extract_channels(img):

    nRows, nCols = img.shape[0], img.shape[1]

    b_channel, g_channel, r_channel= np.zeros((nRows, nCols), dtype=np.uint8), np.zeros((nRows, nCols), dtype=np.uint8), np.zeros((nRows, nCols), dtype=np.uint8)

    for i in range(nRows):
        for j in range(nCols):
            b_channel[i][j] = img[i][j][0]
            g_channel[i][j] = img[i][j][1]
            r_channel[i][j] = img[i][j][2]

    return (b_channel, g_channel, r_channel)

img = cv.imread('image.jpg')

(blue_img, green_img, red_img) = extract_channels(img)

cv.imshow('Display Blue', blue_img)
key = cv.waitKey(0)

cv.imshow('Display Green', green_img)
key = cv.waitKey(0)

cv.imshow('Display Red', red_img)
key = cv.waitKey(0)